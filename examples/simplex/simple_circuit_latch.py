"""simple_circuit_latch.py
Demonstrate an SR latch using combinators with simplex helpers.
"""

from draftsman.simplex import Blueprint


def main() -> None:
    bp = Blueprint()
    set_decider = bp.add_entity(
        "decider-combinator",
        (0, 0),
        control_behavior={
            "decider_conditions": {
                "first_signal": "signal-S",
                "comparator": "!=",
                "constant": 0,
                "output_signal": "signal-L",
                "copy_count_from_input": False,
            }
        },
    )
    reset_decider = bp.add_entity(
        "decider-combinator",
        (2, 0),
        control_behavior={
            "decider_conditions": {
                "first_signal": "signal-R",
                "comparator": "!=",
                "constant": 0,
                "output_signal": "signal-L",
                "copy_count_from_input": False,
            }
        },
    )
    latch = bp.add_entity(
        "arithmetic-combinator",
        (1, 1),
        control_behavior={
            "arithmetic_conditions": {
                "first_signal": "signal-L",
                "operation": "+",
                "second_signal": "signal-S",
                "output_signal": "signal-L",
            }
        },
    )
    bp.add_circuit_connection("red", set_decider, latch)
    bp.add_circuit_connection("red", latch, reset_decider)
    bp.add_circuit_connection("red", reset_decider, set_decider)
    print(bp.to_string())


if __name__ == "__main__":
    main()
