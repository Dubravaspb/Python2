class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает следующий id для добавления новой книги.
        Если книг нет, возвращает 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по её id.
        Если книга не найдена, вызывает ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования классов
if __name__ == '__main__':
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    # Создаем пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Ожидается 1

    # Создаем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Создаем библиотеку с книгами
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Ожидается 3

    # Проверяем индекс книги по id
    print(library_with_books.get_index_by_book_id(1))  # Ожидается 0

    # Проверяем вызов ошибки при отсутствии книги
    try:
        library_with_books.get_index_by_book_id(3)
    except ValueError:
        pass
