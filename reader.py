from ebooklib import epub

class EPUBBook:
    def __init__(self, epub_path):
        self.book = epub.read_epub(epub_path)
        self.chapters = [item.get_content().decode("utf-8") 
                         for item in self.book.get_items() 
                         if item.get_type() == epub.EpubHtml]
        self.current_index = 0

    def get_current_chapter(self):
        if 0 <= self.current_index < len(self.chapters):
            return self.chapters[self.current_index]
        return ""

    def next_chapter(self):
        if self.current_index < len(self.chapters) - 1:
            self.current_index += 1
        return self.get_current_chapter()

    def prev_chapter(self):
        if self.current_index > 0:
            self.current_index -= 1
        return self.get_current_chapter()

    def jump_to(self, index):
        if 0 <= index < len(self.chapters):
            self.current_index = index
        return self.get_current_chapter()

    def total_chapters(self):
        return len(self.chapters)

    def current_position(self):
        return self.current_index + 1
