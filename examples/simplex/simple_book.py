# simple_book.py
"""
Create a blueprint book with two empty blueprints using simplex.
"""

from draftsman.simplex import Blueprint, BlueprintBook


def main() -> None:
    bp1 = Blueprint()
    bp2 = Blueprint()

    book = BlueprintBook([bp1, bp2])
    print(len(book.blueprints))


if __name__ == "__main__":
    main()
