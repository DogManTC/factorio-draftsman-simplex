"""mix_beacon_factory.py
Blueprint a beaconed assembler setup using both APIs.
"""

from draftsman.simplex import Blueprint
from draftsman.entity import Beacon


def main() -> None:
    bp = Blueprint()
    assembler = bp.add_entity("assembling-machine-1", (0, 0))
    for dx in (-2, 2):
        bp.entities.append(Beacon(position=(dx, 0)))
    bp.set_recipe(assembler, "electronic-circuit")
    print(bp.to_string())


if __name__ == "__main__":
    main()
