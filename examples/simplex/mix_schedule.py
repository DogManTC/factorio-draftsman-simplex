# mix_schedule.py
"""
Create a train with a schedule using both simplex and the core API.
"""

from draftsman.simplex import Blueprint
from draftsman.rail import Schedule, WaitCondition


def main() -> None:
    bp = Blueprint()
    schedule = Schedule([WaitCondition("inactivity", 300)])
    bp.schedules[0] = schedule
    print(bp.schedules[0].wait_conditions[0].type)


if __name__ == "__main__":
    main()
