"""Simplified helper interface for Draftsman.

This module exposes a thin layer of convenience functions on top of the
regular Draftsman API.  All underlying functionality remains available
but common tasks such as loading or saving blueprints require less code.
"""

from __future__ import annotations

import json
import os
from typing import Union

from draftsman.blueprintable import (
    Blueprint,
    BlueprintBook,
    get_blueprintable_from_string,
)
from draftsman.env import update as _update

__all__ = [
    "Blueprint",
    "BlueprintBook",
    "load",
    "load_blueprint",
    "save_blueprint",
    "setup",
]


# ---------------------------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------------------------

def setup(mods_path: str | None = None, *, factorio_version: str | None = None, verbose: bool = False) -> None:
    """Update Draftsman's data using :func:`draftsman.env.update`.

    Parameters
    ----------
    mods_path:
        Optional path to the directory containing Factorio mods.
    factorio_version:
        Desired Factorio version string. If omitted, the version bundled with
        Draftsman is used.
    verbose:
        If ``True`` prints progress information while updating the data.
    """
    _update(verbose=verbose, mods_path=mods_path, factorio_version=factorio_version)


# ---------------------------------------------------------------------------
# Blueprint helpers
# ---------------------------------------------------------------------------

def load_blueprint(source: str | os.PathLike) -> Blueprint:
    """Create a :class:`~draftsman.classes.blueprint.Blueprint` from a blueprint
    string or from a JSON/file path.
    """
    if os.path.exists(source):
        with open(source, "r", encoding="utf-8") as fh:
            data = fh.read()
    else:
        data = source

    if data.lstrip().startswith("{"):
        return Blueprint(json.loads(data))
    return Blueprint(data)


def save_blueprint(blueprint: Blueprint, path: str | os.PathLike) -> None:
    """Write ``blueprint`` to ``path`` as a blueprint string."""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(blueprint.to_string())


def load(source: str) -> Union[Blueprint, BlueprintBook]:
    """Load any blueprintable object from ``source``.

    Parameters
    ----------
    source:
        Blueprint string to decode. The correct object type is returned
        automatically.
    """
    return get_blueprintable_from_string(source)

