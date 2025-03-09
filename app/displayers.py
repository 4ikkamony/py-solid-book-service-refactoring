from abc import ABC, abstractmethod

from app.protocols import HasContent


class Displayer(ABC):
    @staticmethod
    @abstractmethod
    def display(obj: HasContent) -> None:
        pass


class ConsoleDisplayer(Displayer):
    @staticmethod
    def display(obj: HasContent) -> None:
        print(obj.content)


class ReverseDisplayer(Displayer):
    @staticmethod
    def display(obj: HasContent) -> None:
        print(obj.content[::-1])
