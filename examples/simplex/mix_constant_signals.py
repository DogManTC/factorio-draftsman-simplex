# mix_constant_signals.py
"""
Populate a constant combinator using simplex and raw entities.
"""

from draftsman.simplex import Blueprint
from draftsman.entity import ConstantCombinator


def main() -> None:
    bp = Blueprint()
    cc = ConstantCombinator("constant-combinator")
    cc.set_signal(1, "iron-plate", 100)
    bp.entities.append(cc)
    print(cc.get_signal(1))


if __name__ == "__main__":
    main()
