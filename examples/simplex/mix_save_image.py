# mix_save_image.py
"""
Render a blueprint with pillow after creating it via simplex.
"""

from draftsman.simplex import Blueprint
from draftsman.utilities import BlueprintImage


def main() -> None:
    bp = Blueprint()
    bp.add_entity("stone-wall", (0, 0))
    img = BlueprintImage.from_blueprint(bp)
    img.image.save("preview.png")
    print(img.image.size)


if __name__ == "__main__":
    main()
