"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting.Selection (from SpaceClaim API docs).
"""

from __future__ import annotations

class ISelection:
    """ISelection stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes ISelection. Auto-generated stub."""
        pass

    @property
    def Items(self):
        pass

    def SetActive(self, *args, **kwargs):
        pass

    def IsValid(self, *args, **kwargs):
        pass


class ISelectionCollection:
    """ISelectionCollection stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes ISelectionCollection. Auto-generated stub."""
        pass

    def Subtract(self, selectionObject):
        pass

    def Add(self, selectionObject):
        pass


class Selection:
    """Selection stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes Selection. Auto-generated stub."""
        pass

    @property
    def Items(self):
        pass

    def op_Addition(self, s1, s2):
        pass

    def CreatePowerSeletionByNames(self, names):
        pass

    def SetActive(self, *args, **kwargs):
        pass

    def GoSelect(self, *args, **kwargs):
        pass

    def CreatePowerSelectionByGroups(self, groupNames):
        pass

    def CreatePowerSelectionByIds(self, ids):
        pass

    def Create(self, docObjects):
        pass

    def CreateByGroups(self, groupNames):
        pass

    def CreateByNames(self, names):
        pass

    def Create(self, docObjects):
        pass

    def CreateByIds(self, ids):
        pass

    def CreateSelectionPower(self, docObjects):
        pass

    def IsValid(self, *args, **kwargs):
        pass

    def CreateSelectionPower(self, docObjects):
        pass

    def op_Subtraction(self, s1, s2):
        pass

    def CreateSelectionPower(self, docObject):
        pass

    def GetActive(self, *args, **kwargs):
        pass

    def Create(self, docObject):
        pass

