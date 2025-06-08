"""simple_mall.py
Lay out assemblers for a small starter mall using simplex.
"""

from draftsman.simplex import Blueprint

ITEMS = [
    "transport-belt",
    "inserter",
    "assembling-machine-1",
    "stone-furnace",
]


def main() -> None:
    bp = Blueprint()
    for i, item in enumerate(ITEMS):
        machine = bp.add_entity("assembling-machine-1", (i * 3, 0))
        bp.set_recipe(machine, item)
        bp.add_entity("steel-chest", (i * 3, 2))
    print(bp.to_string())


if __name__ == "__main__":
    main()
