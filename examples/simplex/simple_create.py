# simple_create.py
"""
Create a blueprint with a single chest using the simplex helpers.
"""

from draftsman.simplex import Blueprint


def main() -> None:
    bp = Blueprint()
    bp.add_entity("steel-chest", (0, 0))
    print(bp.to_string())


if __name__ == "__main__":
    main()
