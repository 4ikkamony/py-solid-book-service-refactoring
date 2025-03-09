from app.book import Book
from app.printers import BookConsolePrinter, BookReversePrinter
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.serializers import JsonSerializer, BookXmlSerializer


ACTIONS = {
    "display": {
        "console": ConsoleDisplayer.display,
        "reverse": ReverseDisplayer.display,
    },
    "print": {
        "console": BookConsolePrinter.print,
        "reverse": BookReversePrinter.print,
    },
    "serialize": {
        "json": JsonSerializer.serialize,
        "xml": BookXmlSerializer.serialize,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:

        if cmd not in ACTIONS:
            raise ValueError(
                f"No such command '{cmd}'"
            )

        if method_type not in ACTIONS[cmd]:
            raise ValueError(
                f"Command '{cmd}' has no such method type '{method_type}'"
            )

        action = ACTIONS[cmd][method_type]

        result = action(book)

        if cmd == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
