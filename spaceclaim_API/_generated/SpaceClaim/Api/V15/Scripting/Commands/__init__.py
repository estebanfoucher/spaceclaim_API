"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting.Commands (from SpaceClaim API docs).
"""

from __future__ import annotations

class BlockBody:
    """Creates a solid block."""

    def __init__(self, *args, **kwargs):
        """Initializes BlockBody. Auto-generated stub."""
        pass

    def Create(self, startPoint, endPoint):
        """Creates a solid block with the specified points."""
        pass


class CircularSurface:
    """Creates a circular surface."""

    def __init__(self, *args, **kwargs):
        """Initializes CircularSurface. Auto-generated stub."""
        pass

    def Create(self, radius, zDir, origin):
        """Creates a circular surface with a specified radius."""
        pass


class ClosestPoint:
    """Calculates the closest point on a target body given a source point"""

    def __init__(self, *args, **kwargs):
        """Initializes ClosestPoint. Auto-generated stub."""
        pass

    def Get(self, targetBody, sourcePoint):
        """Gets the closest point on the given target body."""
        pass

    def Get(self, targetFace, sourcePoint):
        """Gets the closest point on the given target face."""
        pass

    def Get(self, targetEdge, sourcePoint):
        """Gets the closest point on the given target edge."""
        pass

    def Get(self, targetCurve, sourcePoint):
        """Gets the closest point on the given target curve."""
        pass


class ClosestPointCurveResult:
    """Gets the object containing the closest point."""

    def __init__(self, *args, **kwargs):
        """Initializes ClosestPointCurveResult. Auto-generated stub."""
        pass

    @property
    def Parent(self):
        """Gets the object containing the closest point."""
        pass

    @property
    def Point(self):
        """The point on the curve."""
        pass


class ClosestPointResult:
    """Gets the object containing the closest point."""

    def __init__(self, *args, **kwargs):
        """Initializes ClosestPointResult. Auto-generated stub."""
        pass

    @property
    def Parent(self):
        """Gets the object containing the closest point."""
        pass

    @property
    def Point(self):
        """Gets the closest point."""
        pass


class ClosestPointSurfaceResult:
    """Gets the object containing the closest point."""

    def __init__(self, *args, **kwargs):
        """Initializes ClosestPointSurfaceResult. Auto-generated stub."""
        pass

    @property
    def Parent(self):
        """Gets the object containing the closest point."""
        pass

    @property
    def Point(self):
        """Gets the point on the surface."""
        pass


class Combine:
    """Merge or spilt objects or bodies."""

    def __init__(self, *args, **kwargs):
        """Initializes Combine. Auto-generated stub."""
        pass

    def Merge(self, targetSelection, toolSelection):
        """Add or merge the objects together."""
        pass

    def Intersect(self, target, tool, options):
        """Subtract or split objects or bodies from each other."""
        pass

    def RemoveRegions(self, selection):
        """Removes the selected region."""
        pass

    def Intersect(self, target, tool, options):
        """Subtract or split objects or bodies from each other."""
        pass


class ConstantFillet:
    """Fillets a DesignEdge or DesignFace with a given constant radius"""

    def __init__(self, *args, **kwargs):
        """Initializes ConstantFillet. Auto-generated stub."""
        pass

    def Execute(self, selectObject, blendRadius):
        """Executes a constant radius fillet given set of Faces or Edges in a object"""
        pass

    def Execute(self, selectObject, blendRadius, options):
        """Executes a constant radius fillet given set of Faces or Edges in a object"""
        pass


class Copy:
    """Copies a selection to the clipboard"""

    def __init__(self, *args, **kwargs):
        """Initializes Copy. Auto-generated stub."""
        pass

    def ToClipboard(self, selection):
        pass


class CurveGapProblemArea:
    """Curve gap problem area"""

    def __init__(self, *args, **kwargs):
        """Initializes CurveGapProblemArea. Auto-generated stub."""
        pass


class CurveGaps:
    """Finds and repairs curve gaps"""

    def __init__(self, *args, **kwargs):
        """Initializes CurveGaps. Auto-generated stub."""
        pass

    def FixSpecific(self, specifics):
        """Fixes a gap based on specified edge points"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds curve gaps"""
        pass

    def FindAndFix(self, workField, opts):
        """Finds and fixes gas in curves given a working field"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes curve gaps in calculated ProblemAreas"""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes gas in curves in current part"""
        pass


class CylinderBody:
    """Creates a solid cylinder."""

    def __init__(self, *args, **kwargs):
        """Initializes CylinderBody. Auto-generated stub."""
        pass

    def Create(self, centerpoint, endPoint, dragPoint, extrudeMode):
        """Creates a solid cylinder."""
        pass


class DatumLineCreator:
    """Creates a DatumLine"""

    def __init__(self, *args, **kwargs):
        """Initializes DatumLineCreator. Auto-generated stub."""
        pass

    def Create(self, selection, select):
        """Creates a DatumLine determined by the selection."""
        pass

    def Create(self, point, direction, select):
        """Creates the DatumLine determined by the specified point and direction."""
        pass

    def Create(self, line, select):
        """Creates a DatumLine determined by the specified Line."""
        pass

    def CreateLineFromSelection(self, selection):
        """Creates a line from selection."""
        pass


class DatumOriginCreator:
    """Creates a CoordinateSystem"""

    def __init__(self, *args, **kwargs):
        """Initializes DatumOriginCreator. Auto-generated stub."""
        pass

    def Create(self, origin, xDir, yDir):
        """Creates an origin from the given point, x-direction and y-direction."""
        pass

    def Create(self, origin, direction):
        """Creates an origin from the given point and z-direction."""
        pass

    def Create(self, frame):
        """Creates an origin defined by the given frame"""
        pass


class DatumPlaneCreator:
    """Creates a DatumPlane"""

    def __init__(self, *args, **kwargs):
        """Initializes DatumPlaneCreator. Auto-generated stub."""
        pass

    def CreatePlaneFromSelection(self, selectionObject):
        """Gets the plane from the selection."""
        pass

    def Create(self, reference, select):
        """Creates a plane from the given selection."""
        pass

    def Create(self, origin, zDir, select):
        """Creates a plane with the specified origin and normal direction."""
        pass

    def Create(self, frame, select):
        """Creates a DatumPlane from the specified frame."""
        pass

    def Create(self, plane, select):
        """Creates a DatumPlane from the specified plane."""
        pass


class DatumPointCreator:
    """Creates a DatumPoint"""

    def __init__(self, *args, **kwargs):
        """Initializes DatumPointCreator. Auto-generated stub."""
        pass

    def Create(self, face, u, v, select):
        """Creates a point from the specified face and parameters."""
        pass

    def Create(self, obj, u, v, select):
        """Creates a point from the specified DocObject and parameters -- the DocObject can only be a face or edge."""
        pass

    def Create(self, edge, u, select):
        """Creates a point from the specified edge and parameter."""
        pass

    def Create(self, point, select):
        """Creates a DatumPoint at the specified point."""
        pass

    def Create(self, sel, u, v, select):
        """Creates a point from the given selection and parameters -- selection must contain a face or edge."""
        pass


class DuplicateCurveProblemArea:
    """Curve gap problem area"""

    def __init__(self, *args, **kwargs):
        """Initializes DuplicateCurveProblemArea. Auto-generated stub."""
        pass


class DuplicateCurves:
    """Finds and removes duplicate curves"""

    def __init__(self, *args, **kwargs):
        """Initializes DuplicateCurves. Auto-generated stub."""
        pass

    def FixSpecific(self, specifics):
        """Fixes a gap based on specified edge points"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds duplicate curves"""
        pass

    def FindAndFix(self, workField, opts):
        """Finds and removes duplicate curves given a working field"""
        pass

    def FindAndFix(self, opts):
        """Finds and removes duplicate curves in current part"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes curve gaps in calculated ProblemAreas"""
        pass


class DuplicateFaces:
    """Finds and repairs duplicate faces"""

    def __init__(self, *args, **kwargs):
        """Initializes DuplicateFaces. Auto-generated stub."""
        pass

    @property
    def MaxGap(self):
        pass

    def FindProblemAreas(self, *args, **kwargs):
        pass

    def FindAndFix(self, opts):
        pass

    def FixSpecific(self, specifics):
        pass

    def Fix(self, *args, **kwargs):
        pass

    def Fix(self, selectObject):
        pass

    def FindAndFix(self, selectObject, opts):
        pass


class Enclosure:
    """Extracts beam form solid"""

    def __init__(self, *args, **kwargs):
        """Initializes Enclosure. Auto-generated stub."""
        pass

    @property
    def EnclosureCushion(self):
        """Gets or sets the enclosure cushion"""
        pass

    def Execute(self, *args, **kwargs):
        """Executes this command"""
        pass

    def Create(self, selection, options):
        """Creates enclosure around selection"""
        pass


class ExtendableSurfaces:
    """Finds and fixes extendable surfaces in modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtendableSurfaces. Auto-generated stub."""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes extendable surfaces in all visible bodies"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the problem areas found by previous FindProblemAreas call"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas"""
        pass

    def FindAndFix(self, selectObject, opts):
        """Finds and fixes extendable surfaces given specific bodies"""
        pass

    def FixSpecific(self, specifics, opts):
        """Fixes specific extendable surfaces gaps denoted by a list of open edges"""
        pass


class ExtraEdges:
    """Finds and fixes extra edges in modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtraEdges. Auto-generated stub."""
        pass

    def FixSpecific(self, selectObject):
        """Fixes the edges given by Selection object"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the problem areas found by previous FindProblemAreas call"""
        pass

    def FindAndFix(self, selectObject, opts):
        """Finds and fixes extra edges in the bodies given in the selection object"""
        pass

    def FixSpecific(self, specifics):
        """Fixes the edges given by the list DocObject list"""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes extra edges among all visible bodies"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas"""
        pass


class ExtractBeam:
    """Extracts beam form solid"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtractBeam. Auto-generated stub."""
        pass

    def Create(self, selection):
        """Extract beams from selected bodies"""
        pass


class ExtrudeEdges:
    """Extrudes a given set of edges"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeEdges. Auto-generated stub."""
        pass

    def Execute(self, selectObject, location, direction, distance, options):
        """Extrudes given set of edges in a"""
        pass


class ExtrudeFaces:
    """Extrudes a given set of faces"""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeFaces. Auto-generated stub."""
        pass

    def Execute(self, selectObject, direction, distance, options):
        """Extrudes given set of faces in a object.The edges provided in act as constraints"""
        pass


class ExtrudeProfile:
    """Extrudes a profile and creates solid body."""

    def __init__(self, *args, **kwargs):
        """Initializes ExtrudeProfile. Auto-generated stub."""
        pass

    def Execute(self, profile, distance, parent, name):
        """Creates a solid body by extruding the given profile up to the given distance."""
        pass


class Fill:
    """Initializes a new instance of the Fill class"""

    def __init__(self, *args, **kwargs):
        """Initializes Fill. Auto-generated stub."""
        pass

    def Execute(self, selection, secondarySelection, fillOptions, mode):
        """Fill the given selection according to the optional arguments"""
        pass


class FillMode:
    """FillMode stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes FillMode. Auto-generated stub."""
        pass


class FillOptions:
    """Initializes a new instance of the FillOptions class"""

    Default = None

    def __init__(self, *args, **kwargs):
        """Initializes FillOptions. Auto-generated stub."""
        pass

    @property
    def GapAngle(self):
        pass

    @property
    def AllowMultiFacePatch(self):
        pass

    @property
    def GapDistance(self):
        pass

    @property
    def AutoExtendFillArea(self):
        pass

    @property
    def PatchBlend(self):
        pass

    @property
    def ZipLaminarEdges(self):
        pass

    @property
    def UntrimSingleFace(self):
        pass


class FilletInfo:
    """Calculates the fillet information of a given DesignFace"""

    def __init__(self, *args, **kwargs):
        """Initializes FilletInfo. Auto-generated stub."""
        pass

    def Create(self, desFace):
        pass


class FixGaps:
    """Finds and repairs gaps in a model"""

    def __init__(self, *args, **kwargs):
        """Initializes FixGaps. Auto-generated stub."""
        pass

    def FindAndFix(self, selectObject, opts):
        pass

    def FixSpecific(self, specifics):
        pass

    def FindAndFix(self, opts):
        pass

    def FindProblemAreas(self, *args, **kwargs):
        pass

    def Fix(self, selectObject):
        pass

    def Fix(self, *args, **kwargs):
        pass


class FixGapsOptions:
    """Initializes a new instance of the FixGapsOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes FixGapsOptions. Auto-generated stub."""
        pass

    @property
    def FixMethod(self):
        pass

    @property
    def AllowMultiPatch(self):
        pass

    @property
    def Angle(self):
        pass

    @property
    def Distance(self):
        pass


class FixInterference:
    """Initializes a new instance of the FixInterference class"""

    def __init__(self, *args, **kwargs):
        """Initializes FixInterference. Auto-generated stub."""
        pass

    def FindAndFix(self, cutSmallerBody):
        pass

    def FixSpecific(self, specifics):
        pass

    def FindAndFix(self, selectObject, cutSmallerBody):
        pass

    def Fix(self, *args, **kwargs):
        pass

    def FindProblemAreas(self, *args, **kwargs):
        pass

    def Fix(self, selectObject):
        pass


class HandleAxis:
    """HandleAxis stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes HandleAxis. Auto-generated stub."""
        pass


class IClosestPointResult:
    """IClosestPointResult stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes IClosestPointResult. Auto-generated stub."""
        pass

    @property
    def Point(self):
        pass

    @property
    def Parent(self):
        pass


class Midsurface:
    """Calculates the midsurface of a body"""

    def __init__(self, *args, **kwargs):
        """Initializes Midsurface. Auto-generated stub."""
        pass

    def GetMatchingFacePairs(self, face1, face2, thicknessTolerance):
        """Finds all faces with the same offset as the faces provided."""
        pass

    def GetMatchingFacePairs(self, pair, thicknessTolerance):
        """Finds all faces with the same offset as the faces provided."""
        pass

    def GetMatchingFacePairs(self, selection, thicknessTolerance):
        """Finds all faces with the same offset as the faces in the given selection."""
        pass

    def Create(self, faces, options):
        """Creates the midsurface based on the provided face pairs."""
        pass

    def GetFacePairsByRange(self, selection, min, max):
        """Find all face pairs with offset within the provided range."""
        pass

    def GetFacePairsByRange(self, face, min, max):
        """Find all face pairs with offset within the provided range."""
        pass


class MidsurfaceFacePair:
    """Pair of faces to be used to find the mid-surface of a body."""

    def __init__(self, *args, **kwargs):
        """Initializes MidsurfaceFacePair. Auto-generated stub."""
        pass

    @property
    def Face1(self):
        """Gets the first face."""
        pass

    @property
    def Face2(self):
        """Gets the second face."""
        pass

    def Create(self, selection):
        """Creates a MidsurfaceFacePair based on selection."""
        pass

    def Flip(self, *args, **kwargs):
        """Flips the faces."""
        pass

    def Create(self, desFace1, desFace2):
        """Creates a MidsurfaceFacePair from the specified faces."""
        pass


class MissingFaces:
    """Finds and fixes missing faces in modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes MissingFaces. Auto-generated stub."""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes missing faces in all visible bodies"""
        pass

    def FixSpecific(self, specifics, opts):
        """Fixes specific missing faces gaps denoted by a list of open edges"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas"""
        pass

    def FindAndFix(self, selectObject, opts):
        """Finds and fixes missing faces given specific bodies"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the problem areas found by previous FindProblemAreas call"""
        pass


class MoveImprintEdges:
    """Moves a given set of edges imprinted on a surface"""

    def __init__(self, *args, **kwargs):
        """Initializes MoveImprintEdges. Auto-generated stub."""
        pass

    def Execute(self, selectObject, location, direction, distance, options):
        """Moves given set of edges imprinted on a surfce in a"""
        pass


class OffsetEdges:
    """Offsets a given set of edges"""

    def __init__(self, *args, **kwargs):
        """Initializes OffsetEdges. Auto-generated stub."""
        pass

    def Execute(self, selectObject, offset):
        """Offsets given set of edges in a"""
        pass


class OffsetFaces:
    """Offsets a given set of faces"""

    def __init__(self, *args, **kwargs):
        """Initializes OffsetFaces. Auto-generated stub."""
        pass

    def Execute(self, selectObject, offset, options):
        """Offsets given set of faces in a object"""
        pass

    def Execute(self, selectObject, offset, direction, options):
        """Offsets a given set of faces in a object in a given"""
        pass


class OffsetRelation:
    """Sets the offset relation and changes the thickness."""

    def __init__(self, *args, **kwargs):
        """Initializes OffsetRelation. Auto-generated stub."""
        pass

    def ChangeOffset(self, selection, offset, options):
        """Changes the offset between faces having offset relation."""
        pass


class Paste:
    """Pastes from the clipboard"""

    def __init__(self, *args, **kwargs):
        """Initializes Paste. Auto-generated stub."""
        pass

    def FromClipboard(self, *args, **kwargs):
        pass


class PlanarBody:
    """Creates a planar body given a set of curves."""

    def __init__(self, *args, **kwargs):
        """Initializes PlanarBody. Auto-generated stub."""
        pass

    def Create(self, plane, curves, parent, name):
        """Creates the planar body given a plane and a set of curves"""
        pass


class ProblemArea:
    """Initializes a new instance of the ProblemArea class"""

    def __init__(self, *args, **kwargs):
        """Initializes ProblemArea. Auto-generated stub."""
        pass

    @property
    def DocObjects(self):
        pass

    @property
    def Fixed(self):
        pass

    @property
    def Alive(self):
        pass

    @property
    def Excluded(self):
        pass


class RectangularSurface:
    """Creates a rectangular surface."""

    def __init__(self, *args, **kwargs):
        """Initializes RectangularSurface. Auto-generated stub."""
        pass

    def Create(self, width, height, origin):
        """Create rectangle surface with the specified width, height and bottom left corner."""
        pass


class ReplaceFacesWithFace:
    """Replace two or more faces with a single face."""

    def __init__(self, *args, **kwargs):
        """Initializes ReplaceFacesWithFace. Auto-generated stub."""
        pass

    def Execute(self, faces, options):
        """Replace two or more faces with a single face."""
        pass

    def Execute(self, selection, options):
        """Replace two or more faces with a single face."""
        pass


class RevolveFaces:
    """Revolves a given set of Faces about an axis"""

    def __init__(self, *args, **kwargs):
        """Initializes RevolveFaces. Auto-generated stub."""
        pass

    def Execute(self, selectObject, secondarySelection, direction, angle, options):
        pass

    def Execute(self, selectObject, secondarySelection, angle, options):
        """Revolves a given set of Faces in a object about a given axis in a with a specified angle. The edges provided in act as constraints."""
        pass

    def Execute(self, selectObject, axis, angle, options):
        """Revolves a given set of Faces in a object about a given axis with a specified angle. The edges provided in act as constraints."""
        pass


class Scale:
    """Scales a body or a datum with a given vale"""

    def __init__(self, *args, **kwargs):
        """Initializes Scale. Auto-generated stub."""
        pass

    def Execute(self, selectObject, apiOrigin, scale, scalePreserveHoles):
        pass

    def Execute(self, selectObject, apiOrgin, apiDirection, scale, scalePreserveHoles):
        pass

    def Execute(self, selectObject, apiOrigin, apiDirection, scale, scalePreserveHoles):
        pass


class Shell:
    """Shells bodies"""

    def __init__(self, *args, **kwargs):
        """Initializes Shell. Auto-generated stub."""
        pass

    def ShellBodies(self, selection, offset):
        """Shells a given set of bodies from"""
        pass

    def RemoveFaces(self, selection, offset):
        """Shells bodies by removing a given set of faces from a"""
        pass


class ShortEdges:
    """Finds and fixes short edges in modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes ShortEdges. Auto-generated stub."""
        pass

    def FindAndFix(self, options):
        """Finds and fixes short edges in all visible bodies"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas (short edges)"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the short edges found with the previous FindProblemAreas call"""
        pass

    def FixSpecific(self, specifics, opts):
        """Fixes specific short edges given as a list of edges"""
        pass

    def FindAndFix(self, selectObject, options):
        """Finds and fixes short edges in bodies given by a selection object"""
        pass


class SmallFaces:
    """Finds and fixes small faces in modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes SmallFaces. Auto-generated stub."""
        pass

    def FixSpecific(self, specifics):
        """Fixes specific small faces given as a list of faces"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the problem areas found by the previous FindProblemAreas call"""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes small faces in all visible bodies"""
        pass

    def FindAndFix(self, selectObject, opts):
        """Finds and fixes small faces given specific bodies"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas"""
        pass


class SphereBody:
    """Creates a solid sphere."""

    def __init__(self, *args, **kwargs):
        """Initializes SphereBody. Auto-generated stub."""
        pass

    def Create(self, centerpoint, endPoint, extrudeMode):
        """Creates a solid sphere given a center point and end point."""
        pass


class SplitEdges:
    """Find and fixes split edges in a modeling body(s)"""

    def __init__(self, *args, **kwargs):
        """Initializes SplitEdges. Auto-generated stub."""
        pass

    def FixSpecific(self, specifics, opts):
        """Fixes specific split edges denoted by a list of curve points"""
        pass

    def Fix(self, *args, **kwargs):
        """Fixes the problem areas found by previous FindProblemAreas call"""
        pass

    def FindAndFix(self, selectObject, opts):
        """Finds and fixes split edges given specific bodies"""
        pass

    def FindAndFix(self, opts):
        """Finds and fixes split edges in all visible bodies"""
        pass

    def FindProblemAreas(self, *args, **kwargs):
        """Finds the problem areas"""
        pass


class SplitFace:
    """Splits a face along given curves"""

    def __init__(self, *args, **kwargs):
        """Initializes SplitFace. Auto-generated stub."""
        pass

    def Execute(self, *args, **kwargs):
        """Splits the face with the given input curves"""
        pass


class SplitProblemArea:
    """Initializes a new instance of the SplitProblemArea class"""

    def __init__(self, *args, **kwargs):
        """Initializes SplitProblemArea. Auto-generated stub."""
        pass

    @property
    def SplitResult(self):
        pass


class StitchFaces:
    """Stitches a list of faces into a body"""

    def __init__(self, *args, **kwargs):
        """Initializes StitchFaces. Auto-generated stub."""
        pass

    def Execute(self, selectObject, opts):
        pass

    def FindProblemAreas(self, *args, **kwargs):
        pass

    def Fix(self, *args, **kwargs):
        pass

    def Execute(self, opts):
        pass

    def FixSpecific(self, specifics):
        pass


class StitchOptions:
    """Initializes a new instance of the StitchOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes StitchOptions. Auto-generated stub."""
        pass

    @property
    def MaximumDistance(self):
        pass

    @property
    def CheckForCoincidence(self):
        pass


class SurfaceBody:
    """Creates a bounded surface."""

    def __init__(self, *args, **kwargs):
        """Initializes SurfaceBody. Auto-generated stub."""
        pass

    def Create(self, surface, region, parent, name):
        """Creates a bounded surface body from the given base surface."""
        pass


class SweepFaceCommandOptions:
    """Initializes a new instance of the SweepFaceCommandOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes SweepFaceCommandOptions. Auto-generated stub."""
        pass

    @property
    def SweepNormalTrajectory(self):
        pass

    @property
    def ExtrudeType(self):
        pass


class SweepFaces:
    """Initializes a new instance of the SweepFaces class"""

    def __init__(self, *args, **kwargs):
        """Initializes SweepFaces. Auto-generated stub."""
        pass

    def Execute(self, faces, paths, distance, options):
        pass


class ThickenFaces:
    """Thickens a given set of faces"""

    def __init__(self, *args, **kwargs):
        """Initializes ThickenFaces. Auto-generated stub."""
        pass

    def Execute(self, selectObject, direction, value, options):
        """Thickens a given set of faces in a given direction"""
        pass


class Transform:
    """Initializes a new instance of the Transform class"""

    def __init__(self, *args, **kwargs):
        """Initializes Transform. Auto-generated stub."""
        pass

    def Upto(self, selectionObject, uptoObject, apiFrame, axis, options):
        pass

    def OrientTo(self, selectionObject, secondaryselectionObject, apiFrame, axis, options):
        pass

    def MoveRadiallyAboutAxis(self, selectionObject, secondaryselectionObject, uptoObject, options):
        pass

    def CreateFrame(self, selectionObject):
        pass

    def Anchor(self, selectionObject, point):
        pass

    def MoveRadiallyAboutAxis(self, selectionObject, secondaryselectionObject, value, options):
        pass

    def OrientXAlongDirection(self, selectionObject, currentFrame):
        pass

    def Upto(self, selectionObject, uptoObject, apiFrame, options):
        pass

    def TransformAlongTrajectory(self, selectionObject, secondarySelectionObject, value, options):
        pass

    def Execute(self, selectObject, apiFrame, type, value, options):
        pass

    def TransformAlongTrajectory(self, selectionObject, secondarySelectionObject, uptoObject, apiFrame, options):
        pass

    def XYZ(self, selectionObject, x, y, z, apiFrame, options):
        pass

    def TransformAlongTrajectory(self, selectionObject, secondarySelectionObject, apiFrame, apiEnd, options):
        pass


class TransformOptions:
    """Initializes a new instance of the TransformOptions class"""

    def __init__(self, *args, **kwargs):
        """Initializes TransformOptions. Auto-generated stub."""
        pass

    @property
    def MoveSymmetric(self):
        pass

    @property
    def Copy(self):
        pass

    @property
    def KeepBeamFixed(self):
        pass

    @property
    def MaintainOrientation(self):
        pass

    @property
    def DetachFirst(self):
        pass

    @property
    def CreatePatterns(self):
        pass


class TransformType:
    """TransformType stub generated from SpaceClaim docs."""

    def __init__(self, *args, **kwargs):
        """Initializes TransformType. Auto-generated stub."""
        pass


class VolumeExtract:
    """Represents a volume extract of a void space."""

    def __init__(self, *args, **kwargs):
        """Initializes VolumeExtract. Auto-generated stub."""
        pass

    def Create(self, selectObject, options):
        """Creates a volume extract based on selection."""
        pass


class WorkingField:
    """Working field for curve gap fix command"""

    def __init__(self, *args, **kwargs):
        """Initializes WorkingField. Auto-generated stub."""
        pass

