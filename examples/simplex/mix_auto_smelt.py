"""mix_auto_smelt.py
Create an automated smelting column mixing simplex with the core API.
"""

from draftsman.simplex import Blueprint
from draftsman.entity import Inserter, Furnace


def main() -> None:
    bp = Blueprint()
    for i in range(3):
        furnace = Furnace(position=(i * 2, 0))
        bp.entities.append(furnace)
        inserter = Inserter(position=(i * 2, -1))
        bp.entities.append(inserter)
    print(bp.to_string())


if __name__ == "__main__":
    main()
