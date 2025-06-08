"""mix_train_loader.py
Combine simplex helpers with TrainConfiguration to create a train loader.
"""

from draftsman.simplex import Blueprint
from draftsman.objects import TrainConfiguration


def main() -> None:
    bp = Blueprint()
    config = TrainConfiguration("loco-wagon")
    config.add_fuel_request("locomotive", "coal", 10)
    bp.add_train(config, "stop", (0, 0))
    print(bp.to_string())


if __name__ == "__main__":
    main()
