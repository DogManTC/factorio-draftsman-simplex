"""simple_bus_balancer.py
Generate a 4-lane belt balancer using simplex.
"""

from draftsman.simplex import Blueprint


BELT = "transport-belt"


def main() -> None:
    bp = Blueprint()
    # Input belts
    for i in range(4):
        bp.add_entity(BELT, (0, i))
    # Splitters
    splitters = [bp.add_entity("splitter", (1, i)) for i in range(4)]
    for i in range(4):
        bp.add_circuit_connection("red", splitters[i], splitters[(i + 1) % 4])
    # Output belts
    for i in range(4):
        bp.add_entity(BELT, (2, i))
    print(bp.to_string())


if __name__ == "__main__":
    main()
