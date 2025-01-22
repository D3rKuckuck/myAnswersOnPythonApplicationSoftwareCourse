
# ID книг начинаются с цифры один?
class Library():
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self):
        return len(self.books)+1

    def get_index_by_book_id(self, search_id: int):
        if not self.books:
            raise ValueError(
                "Cписок книг пуст")
        for i, name in enumerate(self.books):
            if search_id-1 == i and i:
                return i
            else:
                raise ValueError(
                    "Книги с запрашиваемым id не существует")

bookas = []
library = Library(bookas)
print(library.get_next_book_id())
print(library.get_index_by_book_id(2))