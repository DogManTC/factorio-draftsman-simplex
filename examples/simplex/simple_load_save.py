# simple_load_save.py
"""
Load a blueprint from a file and save it again using simplex.
"""

from draftsman.simplex import Blueprint, load_blueprint, save_blueprint


def main() -> None:
    bp = Blueprint()
    bp.add_entity("small-electric-pole", (0, 0))
    save_blueprint(bp, "temp.txt")

    loaded = load_blueprint("temp.txt")
    print(loaded.label)


if __name__ == "__main__":
    main()
