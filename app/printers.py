from abc import ABC, abstractmethod

from app.protocols import HasTitleAndContent


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print(obj: HasTitleAndContent) -> None:
        pass


class BookConsolePrinter(Printer):
    @staticmethod
    def print(obj: HasTitleAndContent) -> None:
        print(f"Printing the book: {obj.title}...")
        print(obj.content)


class BookReversePrinter(Printer):
    @staticmethod
    def print(obj: HasTitleAndContent) -> None:
        print(f"Printing the book in reverse: {obj.title}...")
        print(obj.content[::-1])
