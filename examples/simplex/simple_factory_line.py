"""simple_factory_line.py
Create a small multi-step production line using simplex helpers.
"""

from draftsman.simplex import Blueprint


def main() -> None:
    bp = Blueprint()
    # ore -> plate
    furnace = bp.add_entity("stone-furnace", (0, 0))
    inserter = bp.add_entity("burner-inserter", (1, 0))
    chest = bp.add_entity("steel-chest", (2, 0))
    bp.add_circuit_connection("red", furnace, inserter)
    # plate -> gear
    assembler_gear = bp.add_entity("assembling-machine-1", (4, 0))
    bp.set_recipe(assembler_gear, "iron-gear-wheel")
    # gear -> transport belt
    assembler_belt = bp.add_entity("assembling-machine-1", (6, 0))
    bp.set_recipe(assembler_belt, "transport-belt")
    print(bp.to_string())


if __name__ == "__main__":
    main()
