import logging
from abc import ABC, abstractmethod
from typing import List

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class Book:
    """
    Клас, що представляє книгу.
    """

    def __init__(self, title: str, author: str, year: str):
        """
        Ініціалізує об'єкт книги.
        :param title: Назва книги
        :param author: Автор книги
        :param year: Рік видання
        """
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) -> str:
        """
        Повертає рядкове представлення книги.
        :return: Форматований рядок з інформацією про книгу
        """
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    """
    Абстрактний інтерфейс бібліотеки.
    """

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """
        Додає книгу до бібліотеки.
        :param book: Об'єкт книги
        """
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """
        Видаляє книгу з бібліотеки за назвою.
        :param title: Назва книги
        """
        pass

    @abstractmethod
    def show_books(self) -> None:
        """
        Відображає список усіх книг у бібліотеці.
        """
        pass


class Library(LibraryInterface):
    """
    Реалізація бібліотеки.
    """

    def __init__(self) -> None:
        """
        Ініціалізує об'єкт бібліотеки з порожнім списком книг.
        """
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """
        Додає книгу до бібліотеки.
        :param book: Об'єкт книги
        """
        self._books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        """
        Видаляє книгу з бібліотеки за назвою.
        :param title: Назва книги
        """
        book_to_remove = next(
            (book for book in self._books if book.title == title), None
        )
        if book_to_remove:
            self._books.remove(book_to_remove)
            logger.info(f"Book removed: {book_to_remove}")
        else:
            logger.info(f"Book with title '{title}' not found.")

    def show_books(self) -> None:
        """
        Відображає список усіх книг у бібліотеці.
        """
        if not self._books:
            logger.info("No books in the library.")
        for book in self._books:
            print(book)


class LibraryManager:
    """
    Клас, що управляє бібліотекою.
    """

    def __init__(self, library: LibraryInterface) -> None:
        """
        Ініціалізує менеджер бібліотеки.
        :param library: Об'єкт бібліотеки, який реалізує LibraryInterface
        """
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Додає книгу до бібліотеки.
        :param title: Назва книги
        :param author: Автор книги
        :param year: Рік видання
        """
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        """
        Видаляє книгу з бібліотеки за назвою.
        :param title: Назва книги
        """
        self.library.remove_book(title)

    def show_books(self) -> None:
        """
        Відображає список усіх книг у бібліотеці.
        """
        self.library.show_books()


# Основна функція для взаємодії з користувачем
def main() -> None:
    """
    Функція для обробки введення користувача та виклику відповідних методів.
    """
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
