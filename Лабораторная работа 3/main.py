class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Свойство для получения названия книги."""
        return self._name

    @property
    def author(self):
        """Свойство для получения автора книги."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, author={self.author})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        """Свойство для получения количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Сеттер для количества страниц с проверкой."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом.")
        self._pages = value

    def __str__(self):
        return f'Бумажная книга: "{self.name}", автор: {self.author}, страниц: {self.pages}'

    def __repr__(self):
        return f'PaperBook(name="{self.name}", author="{self.author}", pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """Свойство для получения продолжительности аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Сеттер для продолжительности с проверкой."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f'Аудиокнига: "{self.name}", автор: {self.author}, продолжительность: {self.duration} ч.'

    def __repr__(self):
        return f'AudioBook(name="{self.name}", author="{self.author}", duration={self.duration})'

if __name__ == "__main__":
    # Создаем объекты
    book = Book("1984", "Джордж Оруэлл")
    paper_book = PaperBook("Мастер и Маргарита", "Михаил Булгаков", 480)
    audio_book = AudioBook("Преступление и наказание", "Федор Достоевский", 19.5)

    # Выводим информацию
    print(book)  # Книга: "1984", автор: Джордж Оруэлл
    print(paper_book)  # Бумажная книга: "Мастер и Маргарита", автор: Михаил Булгаков, страниц: 480
    print(audio_book)  # Аудиокнига: "Преступление и наказание", автор: Федор Достоевский, продолжительность: 19.5 ч.
    print(repr(book))
    print(repr(paper_book))
    print(repr(audio_book))