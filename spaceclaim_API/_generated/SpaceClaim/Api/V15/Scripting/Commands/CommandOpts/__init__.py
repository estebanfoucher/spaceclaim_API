"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting.Commands.CommandOpts (from SpaceClaim API docs).
"""

from __future__ import annotations

class AxisCushion:
    """Defines low/high values for cushion along axis"""

    def __init__(self, *args, **kwargs):
        """Initializes AxisCushion. Auto-generated stub."""
        pass

    @property
    def Low(self):
        """Gets the cushion at the low end of the axis"""
        pass

    @property
    def High(self):
        """Gets the cushion at the high end of the axis"""
        pass


class BaselineOptions:
    """Offset baseline options"""

    def __init__(self, *args, **kwargs):
        """Initializes BaselineOptions. Auto-generated stub."""
        pass


class BoxEnclosureCushion:
    """Defines the enclosure boundaries for a box enclosure"""

    def __init__(self, *args, **kwargs):
        """Initializes BoxEnclosureCushion. Auto-generated stub."""
        pass

    @property
    def YAxis(self):
        """Gets or sets the y axis cushion"""
        pass

    @property
    def XAxis(self):
        """Gets or sets the x axis cushion"""
        pass

    @property
    def ZAxis(self):
        """Gets or sets the z axis cushion"""
        pass

    def ConvertFrom(self, other):
        """Converts from other type enclosure cushion to box enclosure"""
        pass


class CommandOptions:
    """Base CommandOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes CommandOptions. Auto-generated stub."""
        pass


class ConstantFilletOptions:
    """Constant fillet options."""

    def __init__(self, *args, **kwargs):
        """Initializes ConstantFilletOptions. Auto-generated stub."""
        pass


class CreationLocation:
    """Midsurface creation location"""

    def __init__(self, *args, **kwargs):
        """Initializes CreationLocation. Auto-generated stub."""
        pass


class CurveGapsOptions:
    """Curve gaps options"""

    DefaultDistance = None

    def __init__(self, *args, **kwargs):
        """Initializes CurveGapsOptions. Auto-generated stub."""
        pass

    @property
    def Distance(self):
        """Distance between two curves"""
        pass


class CylinderEnclosureCushion:
    """Defines the enclosure boundaries for a cylinder enclosure"""

    def __init__(self, *args, **kwargs):
        """Initializes CylinderEnclosureCushion. Auto-generated stub."""
        pass

    @property
    def Axis(self):
        """Gets or sets the axis cushion"""
        pass

    @property
    def Radius(self):
        """Gets or sets the radius"""
        pass

    def ConvertFrom(self, other):
        """Converts from other type enclosure cushion to cylinder enclosure"""
        pass


class EnclosureOptions:
    """Options for the Enclosure.Create command"""

    def __init__(self, *args, **kwargs):
        """Initializes EnclosureOptions. Auto-generated stub."""
        pass

    @property
    def Frame(self):
        """Gets or sets the enclosure frame"""
        pass

    @property
    def IsSelectable(self):
        """Gets or sets a value indicating whether the enclosure is selectable"""
        pass

    @property
    def EnclosureType(self):
        """Gets or sets the enclosure type"""
        pass

    @property
    def CustomBody(self):
        """Gets or sets the enclosures custom body"""
        pass

    @property
    def Merge(self):
        """Gets or sets a value indicating whether to do Boolean merge"""
        pass

    @property
    def CushionProportion(self):
        """Gets or sets the cushion proportion of the enclosure"""
        pass

    @property
    def EnclosureCushion(self):
        """Gets or sets the enclosure cushion."""
        pass


class EnclosureType:
    """Defines shape of enclosure"""

    def __init__(self, *args, **kwargs):
        """Initializes EnclosureType. Auto-generated stub."""
        pass


class ExtendableSurfacesOptions:
    """Extendable surfaces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtendableSurfacesOptions. Auto-generated stub."""
        pass

    @property
    def AllowPartialIntersection(self):
        """Gets or sets a value indicating whether to allow partial intersection."""
        pass

    @property
    def AllowExtendToCurves(self):
        """Gets or sets a value indicating whether to extend surfaces to curves."""
        pass

    @property
    def AllowSameBody(self):
        """Gets or sets a value indicating whether to extend surfaces on the same body."""
        pass

    @property
    def Merge(self):
        """Gets or sets a value indicating whether to merge after extend."""
        pass

    @property
    def TrimSurface(self):
        """Gets or sets a value indicating whether to allow trim surface."""
        pass

    @property
    def Distance(self):
        """Gets or sets the maximum distance between surfaces."""
        pass


class ExtrudeEdgeOptions:
    """Extrude edges options class"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeEdgeOptions. Auto-generated stub."""
        pass

    @property
    def ExtrudeType(self):
        """Option to specify the type of extrusion"""
        pass

    @property
    def PullSymmetric(self):
        """option to pull both sides of the edge or surface at once."""
        pass

    @property
    def Copy(self):
        """Copies the edge and moves it instead of extruding the original edge if true"""
        pass


class ExtrudeFaceOptions:
    """Extrude faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeFaceOptions. Auto-generated stub."""
        pass

    @property
    def OffsetMode(self):
        """Option indicating how the relation between faces should be handled"""
        pass

    @property
    def PullSymmetric(self):
        """Pulls symetrically on both sides if true"""
        pass

    @property
    def Copy(self):
        """Copies the face and moves it instead of extruding the original face if true"""
        pass

    @property
    def ExtrudeType(self):
        pass


class ExtrudeType:
    """ExtrudeType stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeType. Auto-generated stub."""
        pass


class FixMethodsType:
    """Different fix method types for missing faces"""

    def __init__(self, *args, **kwargs):
        """Initializes FixMethodsType. Auto-generated stub."""
        pass


class GeometryCommandOptions:
    """Initializes a new instance of the GeometryCommandOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes GeometryCommandOptions. Auto-generated stub."""
        pass

    @property
    def KeepMirror(self):
        pass

    @property
    def KeepCompositeFaceRelationships(self):
        pass

    @property
    def KeepLayoutSurfaces(self):
        pass


class MakeCurvesOptions:
    """Options to make curves during combine"""

    def __init__(self, *args, **kwargs):
        """Initializes MakeCurvesOptions. Auto-generated stub."""
        pass

    @property
    def ImprintAsEdges(self):
        """Sets or gets whether to imprint curves as edges on the target object where it intersects with the cutter object."""
        pass


class MakeSolidsOptions:
    """Options to make solids during combine"""

    def __init__(self, *args, **kwargs):
        """Initializes MakeSolidsOptions. Auto-generated stub."""
        pass

    @property
    def KeepCutter(self):
        """Sets or gets whether to keep the cutter object."""
        pass

    @property
    def MakeAllRegions(self):
        """Sets or gets whether to cut the target object with the cutter object and the cutter object with the target object"""
        pass


class MidsurfaceOptions:
    """Options for the Midsurface.Create command"""

    def __init__(self, *args, **kwargs):
        """Initializes MidsurfaceOptions. Auto-generated stub."""
        pass

    @property
    def TrimSurfaces(self):
        """Gets or sets a value indicating whether trim surfaces."""
        pass

    @property
    def ExtendSurfaces(self):
        """Gets or sets a value indicating whether to extend surfaces."""
        pass

    @property
    def Group(self):
        """Gets or sets a value indicating whether to group surfaces."""
        pass

    @property
    def AllowNonManifold(self):
        """Gets or sets a value indicating whether non-manifolds are allowed ."""
        pass

    @property
    def CreationLocation(self):
        """Gets or sets the creation location."""
        pass


class MissingFacesOptions:
    """Missing faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes MissingFacesOptions. Auto-generated stub."""
        pass

    @property
    def Angle(self):
        pass

    @property
    def Distance(self):
        pass

    @property
    def AllowMultiPatch(self):
        pass

    @property
    def FixMethod(self):
        pass


class ModificationOptions:
    """Initializes a new instance of the ModificationOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes ModificationOptions. Auto-generated stub."""
        pass

    @property
    def MaintainOffsetRelationships(self):
        pass

    @property
    def MaintainMirrorRelationships(self):
        pass

    @property
    def MaintainConnectivity(self):
        pass


class MoveImprintEdgeMode:
    """MoveImprintEdgeMode stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes MoveImprintEdgeMode. Auto-generated stub."""
        pass


class MoveImprintEdgeOptions:
    """Options class for moving edges imprinted on a surface"""

    def __init__(self, *args, **kwargs):
        """Initializes MoveImprintEdgeOptions. Auto-generated stub."""
        pass

    @property
    def RemoveOriginEdges(self):
        pass

    @property
    def Copy(self):
        """Copies the edge and moves it instead of moving the original edge if true"""
        pass

    @property
    def ExtrudeType(self):
        """Option to specify the type of extrusion"""
        pass

    @property
    def Mode(self):
        pass

    @property
    def PivotPoints(self):
        pass

    @property
    def PullSymmetric(self):
        """option to pull both sides of the edge or surface at once."""
        pass

    @property
    def SkipMinimumThresholdCheck(self):
        pass


class OffsetFaceOptions:
    """Offset faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes OffsetFaceOptions. Auto-generated stub."""
        pass

    @property
    def OffsetMode(self):
        """Option indicating how the relation between faces should be handled"""
        pass

    @property
    def ExtrudeType(self):
        """Option to specify the type of extrusion"""
        pass

    @property
    def Copy(self):
        """Copies the face and moves it instead of offsetting the original face if true"""
        pass


class OffsetMode:
    """OffsetMode stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes OffsetMode. Auto-generated stub."""
        pass


class PullMode:
    """PullMode stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes PullMode. Auto-generated stub."""
        pass


class ReplaceFacesWithFaceOptions:
    """Options for create method."""

    def __init__(self, *args, **kwargs):
        """Initializes ReplaceFacesWithFaceOptions. Auto-generated stub."""
        pass

    @property
    def AllowMultiPatch(self):
        """Gets or sets a value indicating whether [allow multi patch]."""
        pass

    @property
    def FailIfCanFill(self):
        """Gets or sets a value indicating whether [fail if can fill]."""
        pass

    @property
    def TangentFaces(self):
        """Gets or sets the faces to maintain tangency."""
        pass

    @property
    def EnforceClosedLoopCheck(self):
        """Gets or sets a value indicating whether [enforce closed loop check]."""
        pass


class RevolveFaceOptions:
    """Revolve faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes RevolveFaceOptions. Auto-generated stub."""
        pass

    @property
    def ExtrudeType(self):
        """Option to specify the type of extrusion"""
        pass

    @property
    def Copy(self):
        """Copies the face and moves it instead of offsetting the original face if true"""
        pass

    @property
    def PullSymmetric(self):
        """Pulls symetrically on both sides if true"""
        pass


class ShortEdgesOptions:
    """Small faces options class"""

    DefaultMaxEdgeLength = None

    def __init__(self, *args, **kwargs):
        """Initializes ShortEdgesOptions. Auto-generated stub."""
        pass

    @property
    def MaxEdgeLength(self):
        pass


class SmallFacesOptions:
    """Small faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes SmallFacesOptions. Auto-generated stub."""
        pass

    @property
    def Area(self):
        pass

    @property
    def Width(self):
        pass

    @property
    def AreaEnabled(self):
        pass

    @property
    def WidthEnabled(self):
        pass


class SphereEnclosureCushion:
    """Defines the enclosure boundaries for a spherical enclosure"""

    def __init__(self, *args, **kwargs):
        """Initializes SphereEnclosureCushion. Auto-generated stub."""
        pass

    @property
    def Radius(self):
        """Gets or sets the radius."""
        pass

    def ConvertFrom(self, other):
        """Converts from other type enclosure cushion to spherical enclosure"""
        pass


class SplitEdgesOptions:
    """Split edges options class"""

    def __init__(self, *args, **kwargs):
        """Initializes SplitEdgesOptions. Auto-generated stub."""
        pass

    @property
    def MinEdgeAngle(self):
        """Minimum edge angle"""
        pass

    @property
    def MinEdgeAngleEnabled(self):
        """Minimum edge angle enabled"""
        pass

    @property
    def MaxEdgeLength(self):
        """Maximum edge length"""
        pass

    @property
    def MaxEdgeLengthEnabled(self):
        """Maximum edge length option enabled"""
        pass


class ThickenFaceOptions:
    """Thicken faces options class"""

    def __init__(self, *args, **kwargs):
        """Initializes ThickenFaceOptions. Auto-generated stub."""
        pass

    @property
    def ExtrudeType(self):
        """Option to specify the type of extrusion"""
        pass

    @property
    def PullSymmetric(self):
        """Pulls symetrically on both sides if true"""
        pass

    @property
    def SelectDirection(self):
        """Thickens faces in the specified direction if true.OtherWise thickens face in its normal direction"""
        pass


class VolumeExtractOptions:
    """Options for the VolumeExtract.Create command."""

    def __init__(self, *args, **kwargs):
        """Initializes VolumeExtractOptions. Auto-generated stub."""
        pass

    @property
    def ImprintCappingEdges(self):
        """Gets or sets a value indicating whether imprint capping edges."""
        pass

    @property
    def SeedPoint(self):
        """Gets or sets the seed point."""
        pass

    @property
    def MergeCreatedVolume(self):
        """Gets or sets a value indicating whether to merge created volumes."""
        pass

    @property
    def OptionalCapNomBodies(self):
        """Gets or sets the optional cap nom bodies."""
        pass

    @property
    def OptionalCapNomFaces(self):
        """Gets or sets the optional cap nom faces."""
        pass

