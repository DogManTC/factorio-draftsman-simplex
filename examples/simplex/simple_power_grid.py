"""simple_power_grid.py
Assemble a small steam power setup using simplex helpers.
"""

from draftsman.simplex import Blueprint


def main() -> None:
    bp = Blueprint()
    boiler = bp.add_entity("boiler", (0, 0))
    bp.add_entity("steam-engine", (2, 0))
    bp.add_entity("offshore-pump", (-2, 0))
    bp.add_circuit_connection("red", boiler, "steam-engine")
    print(bp.to_string())


if __name__ == "__main__":
    main()
