# mix_entities.py
"""
Use simplex Blueprint with standard entity classes.
"""

from draftsman.simplex import Blueprint
from draftsman.entity import AssemblingMachine


def main() -> None:
    bp = Blueprint()
    assembler = AssemblingMachine("assembling-machine-1")
    bp.entities.append(assembler)
    print(len(bp.entities))


if __name__ == "__main__":
    main()
