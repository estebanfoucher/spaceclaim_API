"""
spaceclaim_API
==============

A stub-only Python package that mirrors the public surface of the SpaceClaim
Scripting API so that you can:

- import SpaceClaim objects and commands in a normal Python IDE
- get autocompletion and avoid linter / type-checker errors

This package does **not** implement any real behavior. All functions and
methods are empty and exist only to satisfy tooling.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Sequence


# ---------------------------------------------------------------------------
# Core geometric / model objects (very lightly stubbed)
# ---------------------------------------------------------------------------


class Face:
    """Represents a face of a body in the SpaceClaim model."""

    def MidPoint(self) -> "PointOnFace":
        """
        Returns a point object representing the midpoint of this face.

        This method is a placeholder stub and does not compute anything.
        """
        pass


class PointOnFace:
    """Represents a point lying on a face."""

    @property
    def Point(self) -> Sequence[float]:
        """
        Gets the XYZ coordinates of this point.

        Returns
        -------
        Sequence[float]
            A 3-element sequence representing X, Y, Z coordinates.
        """
        pass


class Body:
    """Represents a body within a SpaceClaim part."""

    @property
    def Faces(self) -> Iterable[Face]:
        """Gets an iterable of faces belonging to this body."""
        pass


class Part:
    """Represents the root part of the active SpaceClaim document."""

    def GetAllBodies(self) -> List[Body]:
        """Returns all bodies contained in this part."""
        pass


# ---------------------------------------------------------------------------
# Named selection utilities (as used in your example script)
# ---------------------------------------------------------------------------


class Selection:
    """
    Represents a selection of SpaceClaim objects.

    This is a very thin stub; real selection behavior is not implemented.
    """

    @staticmethod
    def Create(*objects) -> "Selection":
        """
        Creates a selection from the given objects.

        Parameters
        ----------
        *objects
            Any SpaceClaim entities to include in the selection (faces, bodies,
            etc.).
        """
        pass


class NamedSelection:
    """
    Provides methods for creating and managing named selections.

    This class is stubbed solely to support scripting in regular Python IDEs.
    """

    @staticmethod
    def Create(source: Selection, mask: Optional[Selection] = None):
        """
        Creates a named selection from the specified source selection.

        Parameters
        ----------
        source : Selection
            Selection containing the objects to include.
        mask : Selection, optional
            Optional selection used as a mask or filter.
        """
        pass

    @staticmethod
    def Rename(old_name: str, new_name: str):
        """
        Renames an existing named selection.

        Parameters
        ----------
        old_name : str
            Current name of the selection.
        new_name : str
            New name to assign.
        """
        pass


# ---------------------------------------------------------------------------
# Command plumbing and basic options/result types
# (names chosen to match the documentation where possible)
# ---------------------------------------------------------------------------


class CommandResult:
    """
    Represents the result of executing a SpaceClaim command.

    This stub currently carries no data and exists only for type completeness.
    """

    pass


class CommandOptions:
    """
    Base class for command options types in the SpaceClaim API.

    In the official API this lives under SpaceClaim.Api.V15.Scripting.Commands
    .CommandOpts.CommandOptions; here we provide it as a simple stub.
    """

    pass


class CurveGapsOptions(CommandOptions):
    """
    Curve gaps options.

    This corresponds to the documented
    SpaceClaim.Api.V15.Scripting.Commands.CommandOpts.CurveGapsOptions type.
    """

    # Static field from the docs: DefaultDistance (Double)
    DefaultDistance: float

    def __init__(self, distance: Optional[float] = None):
        """
        Initializes a new instance of the CurveGapsOptions class.

        Parameters
        ----------
        distance : float, optional
            Distance between two curves. If omitted, DefaultDistance is used.
        """
        pass

    @property
    def Distance(self) -> float:
        """
        Gets the distance between two curves used when fixing curve gaps.

        Returns
        -------
        float
            The distance threshold between curves.
        """
        pass

    @Distance.setter
    def Distance(self, value: float) -> None:
        """
        Sets the distance between two curves used when fixing curve gaps.
        """
        pass


class CurveGaps:
    """
    Provides methods for finding and fixing curve gaps in the current part.

    This roughly corresponds to SpaceClaim.Api.V15.Scripting.Commands.CurveGaps.
    """

    @staticmethod
    def FindAndFix(opts: Optional[CurveGapsOptions] = None) -> CommandResult:
        """
        Finds and fixes gaps in curves in the current part.

        Parameters
        ----------
        opts : CurveGapsOptions, optional
            Curve gap options (for example, gap distance). If omitted,
            default options are used.

        Returns
        -------
        CommandResult
            The result of the command.
        """
        pass

    def FindProblemAreas(self) -> CommandResult:
        """
        Finds curve gaps in the model and records them as problem areas.

        Returns
        -------
        CommandResult
            The result of the operation.
        """
        pass

    def Fix(self) -> CommandResult:
        """
        Fixes curve gaps previously identified as problem areas.

        Returns
        -------
        CommandResult
            The result of the operation.
        """
        pass

    @staticmethod
    def FixSpecific() -> CommandResult:
        """
        Fixes a specific curve gap based on specified edge points.

        The concrete parameters are not modeled here; this stub exists
        only to mirror the documented API surface.
        """
        pass


# ---------------------------------------------------------------------------
# Top-level helpers (as they appear in the scripting environment)
# ---------------------------------------------------------------------------


def GetRootPart() -> Part:
    """
    Returns the root part of the active document.

    This is a top-level helper mirroring the function available in the native
    SpaceClaim scripting environment.
    """
    pass


# Re-export generated namespace root if available so users can do:
#   from spaceclaim_API import SpaceClaim
try:  # pragma: no cover - optional convenience
    from ._generated import SpaceClaim as SpaceClaim  # type: ignore
except Exception:  # pragma: no cover
    SpaceClaim = None  # type: ignore


__all__ = [
    # Geometry / model
    "Face",
    "PointOnFace",
    "Body",
    "Part",
    # Selection helpers
    "Selection",
    "NamedSelection",
    # Command plumbing
    "CommandResult",
    "CommandOptions",
    "CurveGapsOptions",
    "CurveGaps",
    # Top-level helpers
    "GetRootPart",
    # Namespaces
    "SpaceClaim",
]



