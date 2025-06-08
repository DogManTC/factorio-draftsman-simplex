"""mix_logic_counter.py
Emulate a simple incrementing counter using combinators.
"""

from draftsman.simplex import Blueprint
from draftsman.entity import ArithmeticCombinator, ConstantCombinator


def main() -> None:
    bp = Blueprint()
    constant = ConstantCombinator(position=(0, 0))
    constant.set_signal(0, "signal-each", 1)
    counter = ArithmeticCombinator(
        position=(2, 0),
        control_behavior={
            "arithmetic_conditions": {
                "first_signal": "signal-C",
                "operation": "+",
                "constant": 1,
                "output_signal": "signal-C",
            }
        },
    )
    bp.entities.append(constant)
    bp.entities.append(counter)
    bp.add_circuit_connection("red", constant, counter)
    bp.add_circuit_connection("red", counter, counter, 2, 1)
    print(bp.to_string())


if __name__ == "__main__":
    main()
