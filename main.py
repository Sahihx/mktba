import sys
from PyQt5.QtWidgets import QApplication
from git_sync import sync_repo
from library import load_books
from reader import EPUBBook
from ui.main_window import MainWindow

REPO_URL = "https://github.com/Sahihx/mktba-books.git"  # ضع هنا رابط الريبو
LOCAL_PATH = "books_repo"

def main():
    sync_repo(REPO_URL, LOCAL_PATH)
    books = load_books(LOCAL_PATH)

    app = QApplication(sys.argv)
    window = MainWindow(books, EPUBBook)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
