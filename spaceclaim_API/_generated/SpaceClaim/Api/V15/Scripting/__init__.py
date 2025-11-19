"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting (from SpaceClaim API docs).
"""

from __future__ import annotations

class ComponentManager:
    """Helper functions to build, copy and manage"""

    def __init__(self, *args, **kwargs):
        """Initializes ComponentManager. Auto-generated stub."""
        pass

    def SetActive(self, comp):
        """Sets the active"""
        pass

    def MoveBodiesToComponent(self, selections, inComp, copy):
        """Moves a of bodies to an existing component"""
        pass

    def CopyToRoot(self, comp):
        """Copies an existing to the root"""
        pass

    def CreateAtComponent(self, comp, name):
        """Creates a new below the given"""
        pass

    def MakeIndependent(self, comp):
        """Makes a independent of its master (if its an instance)"""
        pass

    def CreateAtRoot(self, name):
        """Creates a new at the root"""
        pass

    def SetRootActive(self, *args, **kwargs):
        """Sets the root part to be the active component"""
        pass

    def SetName(self, inComp, name):
        """Sets the base name of the specified"""
        pass

    def MoveBodiesToComponent(self, docList, inComp, copy):
        """Moves an array of bodies to an existing component"""
        pass

    def SetSuffixName(self, inComp, name):
        """Sets the suffix name of the specified"""
        pass

    def CopyToComponent(self, comp, newComp):
        """Copies an existing below the given"""
        pass

    def DeleteEmptyComponents(self, *args, **kwargs):
        """Deletes all empty in the structure tree"""
        pass

    def GetActive(self, *args, **kwargs):
        """Gets the active"""
        pass


class DesignCurveExtensions:
    """End point of the curve"""

    def __init__(self, *args, **kwargs):
        """Initializes DesignCurveExtensions. Auto-generated stub."""
        pass

    def EvalProportion(self, desCurve, parameter):
        """Evaluates the curve at the specified percentage of the curve parameter."""
        pass

    def Evaluate(self, desCurve, parameter):
        """Evaluates the curve at the specified parameter."""
        pass

    def EndPoint(self, desCurve):
        """End point of the curve"""
        pass

    def MidPoint(self, desCurve):
        """Middle point of the curve."""
        pass

    def StartPoint(self, desCurve):
        """Starting point of the curve."""
        pass


class DesignEdgeExtensions:
    """Ending point of the edge"""

    def __init__(self, *args, **kwargs):
        """Initializes DesignEdgeExtensions. Auto-generated stub."""
        pass

    def Evaluate(self, desEdge, parameter):
        """Evaluates the edge at the specified parameter"""
        pass

    def EdgePoint(self, desEdge, proportion):
        pass

    def EvalProportion(self, desEdge, parameter):
        """Evaluates the edge at a given proportion (0-1) of the edge Interval"""
        pass

    def MidPoint(self, desEdge):
        """Middle point of the edge"""
        pass

    def GetInterval(self, desEdge):
        """Returns the Interval of an edge"""
        pass

    def StartPoint(self, desEdge):
        """Starting point of the edge"""
        pass

    def EndPoint(self, desEdge):
        """Ending point of the edge"""
        pass


class DesignFaceExtensions:
    """Ending point of the face."""

    def __init__(self, *args, **kwargs):
        """Initializes DesignFaceExtensions. Auto-generated stub."""
        pass

    def EndPoint(self, desFace):
        """Ending point of the face."""
        pass

    def MidPoint(self, desFace):
        """Middle point of the face."""
        pass

    def FacePoint(self, desFace, proportionU, proportionV):
        pass

    def FaceCurves(self, selection, faceOrEdgePoint1, edgePoint2):
        pass

    def StartPoint(self, desFace):
        """Starting point of the face."""
        pass

    def IsoCurves(self, desFace, uDirCurve, proportion):
        pass

    def Evaluate(self, desFace, parameterU, parameterV):
        """Evaluates the face at the given U and V parameters."""
        pass

    def EvalProportion(self, desFace, percentageU, percentageV):
        """Evaluates the face at the given percentage of the U and V parameters."""
        pass


class PartExtensions:
    """PartExtensions stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes PartExtensions. Auto-generated stub."""
        pass

    def GetAllBodies(self, part):
        pass

    def GetAllComponents(self, part):
        pass


class ScriptEventManager:
    """Manager class for listening to events on DocObjects and attaching a script function to that event"""

    def __init__(self, *args, **kwargs):
        """Initializes ScriptEventManager. Auto-generated stub."""
        pass

    @property
    def Items(self):
        """List of DocObjects on which an update event can be triggered"""
        pass

    @property
    def CreateSingleInstance(self):
        """Creates an instance of a ScriptEventManager"""
        pass

    @property
    def GroupName(self):
        """Name of the Group containing the DocObjects for update events"""
        pass

    @property
    def Enabled(self):
        """Enable (or disable) the ScriptEventManager to start (or stop) listening for update events"""
        pass

    def Delete(self, *args, **kwargs):
        """Delete this instance of the ScriptEventManager"""
        pass

    def SetCallback(self, incoming):
        """Sets the function to be called when any of the Items gets an update event"""
        pass

