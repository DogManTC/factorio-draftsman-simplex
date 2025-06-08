"""mix_full_process.py
Showcase a complete ore-to-circuit production chain in a blueprint book.
"""

from draftsman.simplex import Blueprint, BlueprintBook


def main() -> None:
    smelt = Blueprint()
    smelt.add_entity("stone-furnace", (0, 0))
    smelt.add_entity("inserter", (1, 0))

    circuits = Blueprint()
    assembler = circuits.add_entity("assembling-machine-1", (0, 0))
    circuits.set_recipe(assembler, "electronic-circuit")

    book = BlueprintBook()
    book.blueprints = [smelt, circuits]
    print(book.to_string())


if __name__ == "__main__":
    main()
