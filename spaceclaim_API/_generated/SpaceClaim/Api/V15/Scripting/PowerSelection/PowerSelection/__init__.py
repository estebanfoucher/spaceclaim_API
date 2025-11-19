"""
Auto-generated stubs for namespace: SpaceClaim.Api.V15.Scripting.PowerSelection.PowerSelection (from SpaceClaim API docs).
"""

from __future__ import annotations

class Bodies:
    """Create power selections bases on bodies"""

    def __init__(self, *args, **kwargs):
        """Initializes Bodies. Auto-generated stub."""
        pass

    def BySurfaceArea(self, *args, **kwargs):
        """Select bodies based on surface area matching defining value and comparison"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select bodies with mesh control element size matching given value and comparison"""
        pass

    def ByColor(self, seed, options):
        """Select bodies with color matching seed"""
        pass

    def AllSolidBodies(self, options):
        """Select all solid bodies defined in selection option"""
        pass

    def ByColor(self, color, options):
        """Select bodies with color matching given color"""
        pass

    def ByVolume(self, *args, **kwargs):
        """Select bodies with volume matching the seed and comparison"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select bodies with mesh control element size matching seed and comparison"""
        pass

    def AllSurfaceBodies(self, options):
        """Select all surface bodies defined in selection options"""
        pass

    def BySurfaceArea(self, *args, **kwargs):
        """Select bodies based on surface area matching seed and comparison"""
        pass

    def WithMeshControl(self, options):
        """Select bodies with mesh control"""
        pass

    def ByVolume(self, *args, **kwargs):
        """Select bodies with volume matching defined value and comparison"""
        pass

    def WithMeshControl(self, seed, options):
        """Select bodies with mesh control"""
        pass


class Edges:
    """Create power selections bases on edges"""

    def __init__(self, *args, **kwargs):
        """Initializes Edges. Auto-generated stub."""
        pass

    def ByLengthAndDirection(self, *args, **kwargs):
        """Select edges matching given length and orientation of seed"""
        pass

    def WithMeshControl(self, seed, options):
        """Select edges with mesh control"""
        pass

    def ByLength(self, *args, **kwargs):
        """Select edges matching length of seed and length comparison"""
        pass

    def ByLengthSameFace(self, *args, **kwargs):
        """Select edges with matching length on the same face"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select edges with matching control size"""
        pass

    def BySurfaceHoleRadius(self, *args, **kwargs):
        """Select holes with matching radii with respect to the seed and comparison"""
        pass

    def ByLengthMatchingConnectingFaces(self, seed, options):
        """Select edges on matching connecting faces"""
        pass

    def ByLength(self, *args, **kwargs):
        """Select edges matching given length and comparison"""
        pass

    def ByLengthSameFace(self, *args, **kwargs):
        """Select edges with matching length on same face with respect to seed"""
        pass

    def ByLengthAndDirection(self, *args, **kwargs):
        """Select edges matching given length and orientation"""
        pass

    def BySurfaceHoleRadius(self, *args, **kwargs):
        """Select holes matching given radius and comparison"""
        pass

    def WithMeshControl(self, options):
        """Select edges with mesh control"""
        pass

    def WithMeshControlDivision(self, *args, **kwargs):
        """Select edges with mesh divisions matching seed and comparison"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select edges with mesh control size matching give value and comparison"""
        pass

    def WithMeshControlDivision(self, *args, **kwargs):
        """Select edges with mesh divisions matching given value and comparison"""
        pass

    def BySurfaceLoops(self, searchBodies):
        """Select edges on surface loops"""
        pass


class Faces:
    """Create power selections bases on bodies"""

    def __init__(self, *args, **kwargs):
        """Initializes Faces. Auto-generated stub."""
        pass

    def ByChamferLength(self, *args, **kwargs):
        """Select chamfers matching given length and comparison"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select faces with mesh control element size matching given size and comparison"""
        pass

    def PatternMember(self, seed, all):
        """Select faces in same pattern as seed"""
        pass

    def Coaxial(self, seed):
        """Select coaxial faces matching seed"""
        pass

    def InnerFaces(self, options):
        """Select inner faces"""
        pass

    def RoundChain(self, seed):
        """Select faces in round chain containing seed"""
        pass

    def WithMeshInflation(self, options):
        """Select faces with mesh inflation"""
        pass

    def BySurfaceHoleRadius(self, *args, **kwargs):
        """Select surface holes matching give radius and comparison"""
        pass

    def ByRoundRadius(self, *args, **kwargs):
        """Select rounds matching give radius and comparison"""
        pass

    def ThinAdjacent(self, seed):
        """Select thin adjacent faces to seed"""
        pass

    def Protrusions(self, seed, boundingEdges):
        """Select faces with protrusions matching seed and bounding edges"""
        pass

    def ByArea(self, *args, **kwargs):
        """Select faces matching given area, comparison and surface type"""
        pass

    def ByChamferLength(self, *args, **kwargs):
        """Select chamfers matching seed length and comparison"""
        pass

    def WithMeshControlSize(self, *args, **kwargs):
        """Select faces with mesh control element size matching seed and comparison"""
        pass

    def BySurfaceHoleRadius(self, *args, **kwargs):
        """Select surface holes matching seed and comparison"""
        pass

    def WithVariableRoundRadius(self, options):
        """Select rounds with variable radii"""
        pass

    def WithMeshInflation(self, seed, options):
        """Select faces with mesh inflation"""
        pass

    def ThinAdjacentSameOffset(self, seed):
        """Select thin adjacent, with same offest with respect to seed"""
        pass

    def Depressions(self, seed, boundingEdges):
        """Select faces with depressions matching seed and bounding edges"""
        pass

    def WithMeshControl(self, options):
        """Select faces with mesh control"""
        pass

    def ByArea(self, *args, **kwargs):
        """Select faces matching given area, comparison and surface type"""
        pass

    def ByRoundRadius(self, *args, **kwargs):
        """Select rounds matching seed radius and comparison"""
        pass

    def WithMeshControl(self, seed, options):
        """Select faces with mesh control"""
        pass

