# mix_blueprint_merge.py
"""
Merge two blueprints using simplex and the EntityList API.
"""

from draftsman.simplex import Blueprint
from draftsman.classes.entity_list import EntityList


def main() -> None:
    a = Blueprint()
    b = Blueprint()
    a.add_entity("stone-wall", (0, 0))
    b.add_entity("stone-wall", (1, 0))
    merged = EntityList.union(a.entities, b.entities)
    print(len(merged))


if __name__ == "__main__":
    main()
