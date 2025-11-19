"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting.PowerSelection (from SpaceClaim API docs).
"""

from __future__ import annotations

class IPowerRelation:
    """Power relation interface -- wraps power selection relation."""

    def __init__(self, *args, **kwargs):
        """Initializes IPowerRelation. Auto-generated stub."""
        pass

    @property
    def Category(self):
        """Gets the category of the relation."""
        pass

    @property
    def Type(self):
        """Gets the type of the relation."""
        pass

    @property
    def SearchOptions(self):
        """Gets the search options of the relation."""
        pass

    @property
    def FullName(self):
        """Gets the full name of the relation."""
        pass

    def Update(self, *args, **kwargs):
        """Updates current selection."""
        pass


class IPowerSelection:
    """Search for selection relations based on seed and/or other search criteria"""

    def __init__(self, *args, **kwargs):
        """Initializes IPowerSelection. Auto-generated stub."""
        pass

    @property
    def InnerSelections(self):
        """Gets the inner selections for group relations."""
        pass

    @property
    def AvailableString(self):
        """Gets a string listing the available selection relations."""
        pass

    @property
    def AvailableCategories(self):
        """Gets the available categories."""
        pass

    @property
    def AvailableTypes(self):
        """Gets the available types."""
        pass

    def TypesPerCategory(self, category):
        """Gets a list of relation types for a given category."""
        pass

    def UpdateAll(self, *args, **kwargs):
        """Updates all selection relations."""
        pass

    def FilterCategory(self, category):
        """Filters the category."""
        pass

    def FilterType(self, type):
        """Filters the type."""
        pass


class PowerSearchOptions:
    """Options object for"""

    def __init__(self, *args, **kwargs):
        """Initializes PowerSearchOptions. Auto-generated stub."""
        pass

    @property
    def OtherBodies(self):
        """Gets the other bodies to search."""
        pass

    @property
    def Seed(self):
        """Gets the seed that defines the selection relations."""
        pass

    @property
    def SelectSeed(self):
        """Gets or sets a value indicating whether to add seed to selection."""
        pass

    @property
    def SearchAllBodies(self):
        """Gets a value indicating whether to search all bodies."""
        pass


class PowerSelection:
    """Search for selection relations based on seed and/or other search criteria. The power selection object is an enumerable of found selection relations."""

    AllSelections = None
    CurrentSelectionIter = None
    FilteredSelection = None

    def __init__(self, *args, **kwargs):
        """Initializes PowerSelection. Auto-generated stub."""
        pass

    @property
    def AvailableCategories(self):
        pass

    @property
    def AvailableTypes(self):
        pass

    @property
    def Category(self):
        pass

    @property
    def Items(self):
        """Gets the selected objects."""
        pass

    @property
    def InnerSelections(self):
        pass

    @property
    def FullName(self):
        pass

    @property
    def Current(self):
        pass

    @property
    def AvailableString(self):
        pass

    @property
    def SearchOptions(self):
        pass

    @property
    def Type(self):
        pass

    @property
    def CurrentSelection(self):
        """Gets the current selection."""
        pass

    def Reset(self, *args, **kwargs):
        pass

    def Update(self, *args, **kwargs):
        pass

    def All(self, refSel, searchOptions, category):
        """Create a power selection that enumerates all selection relations based on given reference relation and search options."""
        pass

    def FilterCategory(self, category):
        pass

    def FilterType(self, type):
        pass

    def IsValid(self, *args, **kwargs):
        """Returns true if selection is valid."""
        pass

    def MoveNext(self, *args, **kwargs):
        pass

    def Dispose(self, *args, **kwargs):
        pass

    def UpdateAll(self, *args, **kwargs):
        pass

    def TypesPerCategory(self, category):
        pass

    def All(self, docObj, searchOptions, category):
        """Create a power selection that enumerates all selection relations based on given doc object and search options."""
        pass

    def SetActive(self, *args, **kwargs):
        """Sets the current relation as the active selection."""
        pass


class PowerSelectionScriptGenerator:
    """Initializes a new instance of the PowerSelectionScriptGenerator class"""

    def __init__(self, *args, **kwargs):
        """Initializes PowerSelectionScriptGenerator. Auto-generated stub."""
        pass

    def BuildSnippets(self, *args, **kwargs):
        pass


class RelationCategory:
    """Relation categories for power selection."""

    def __init__(self, *args, **kwargs):
        """Initializes RelationCategory. Auto-generated stub."""
        pass


class RelationType:
    """Relation types definitions for"""

    def __init__(self, *args, **kwargs):
        """Initializes RelationType. Auto-generated stub."""
        pass

    @property
    def Category(self):
        """Gets the relation category."""
        pass

    @property
    def Description(self):
        """Gets the description of the relation type."""
        pass

    def GetHashCode(self, *args, **kwargs):
        pass

    def ToString(self, *args, **kwargs):
        pass


class SearchCriteria:
    """Search criteria for power selection"""

    def __init__(self, *args, **kwargs):
        """Initializes SearchCriteria. Auto-generated stub."""
        pass

