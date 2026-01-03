from PyQt5.QtWidgets import (
    QWidget, QListWidget, QTextBrowser, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel
)
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, books, read_book_class):
        super().__init__()
        self.books = books
        self.read_book_class = read_book_class
        self.current_book = None
        self.setWindowTitle("EPUB Reader")
        self.resize(900, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # قائمة الكتب
        self.book_list = QListWidget()
        for book in self.books:
            self.book_list.addItem(f"{book['title']} - {book['author']}")
        self.book_list.currentRowChanged.connect(self.load_book)

        # منطقة القراءة
        right_layout = QVBoxLayout()
        self.text_area = QTextBrowser()
        self.text_area.setLayoutDirection(Qt.RightToLeft)
        self.text_area.setReadOnly(True)

        # أزرار التحكم
        btn_layout = QHBoxLayout()
        self.prev_btn = QPushButton("السابق")
        self.next_btn = QPushButton("التالي")
        self.increase_font_btn = QPushButton("تكبير الخط")
        self.decrease_font_btn = QPushButton("تصغير الخط")
        self.position_label = QLabel("الفصل: 0/0")

        self.prev_btn.clicked.connect(self.prev_chapter)
        self.next_btn.clicked.connect(self.next_chapter)
        self.increase_font_btn.clicked.connect(self.increase_font)
        self.decrease_font_btn.clicked.connect(self.decrease_font)

        for btn in [self.prev_btn, self.next_btn, self.increase_font_btn, self.decrease_font_btn, self.position_label]:
            btn_layout.addWidget(btn)

        right_layout.addWidget(self.text_area)
        right_layout.addLayout(btn_layout)

        main_layout.addWidget(self.book_list, 1)
        main_layout.addLayout(right_layout, 3)

        self.setLayout(main_layout)
        self.font_size = 14
        self.text_area.setStyleSheet(f"font-size: {self.font_size}px;")

    def load_book(self, index):
        if index >= 0:
            self.current_book = self.read_book_class(self.books[index]['path'])
            self.update_text()

    def update_text(self):
        if self.current_book:
            self.text_area.setHtml(self.current_book.get_current_chapter())
            self.position_label.setText(f"الفصل: {self.current_book.current_position()}/{self.current_book.total_chapters()}")

    def next_chapter(self):
        if self.current_book:
            self.current_book.next_chapter()
            self.update_text()

    def prev_chapter(self):
        if self.current_book:
            self.current_book.prev_chapter()
            self.update_text()

    def increase_font(self):
        self.font_size += 2
        self.text_area.setStyleSheet(f"font-size: {self.font_size}px;")

    def decrease_font(self):
        if self.font_size > 6:
            self.font_size -= 2
            self.text_area.setStyleSheet(f"font-size: {self.font_size}px;")
