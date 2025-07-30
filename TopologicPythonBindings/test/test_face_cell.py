import pytest
import os

def test_face_creation():
    """Test creation of a Face from a Wire."""
    from topologic_core import Vertex, Edge, Wire, Face

    # Create vertices for a square
    v1 = Vertex.ByCoordinates(0, 0, 0)
    v2 = Vertex.ByCoordinates(10, 0, 0)
    v3 = Vertex.ByCoordinates(10, 10, 0)
    v4 = Vertex.ByCoordinates(0, 10, 0)

    # Create edges
    e1 = Edge.ByStartVertexEndVertex(v1, v2)
    e2 = Edge.ByStartVertexEndVertex(v2, v3)
    e3 = Edge.ByStartVertexEndVertex(v3, v4)
    e4 = Edge.ByStartVertexEndVertex(v4, v1)

    # Create wire
    w = Wire.ByEdges([e1, e2, e3, e4])

    # Create face
    f = Face.ByExternalBoundary(w)

    # Check if the face was created with the correct type
    assert "Face" in str(type(f))

def test_cell_creation():
    """Test creation of a Cell from Faces."""
    from topologic_core import Vertex, Edge, Wire, Face, Cell, Topology

    # Create vertices for a cube
    v1 = Vertex.ByCoordinates(0, 0, 0)
    v2 = Vertex.ByCoordinates(10, 0, 0)
    v3 = Vertex.ByCoordinates(10, 10, 0)
    v4 = Vertex.ByCoordinates(0, 10, 0)
    v5 = Vertex.ByCoordinates(0, 0, 10)
    v6 = Vertex.ByCoordinates(10, 0, 10)
    v7 = Vertex.ByCoordinates(10, 10, 10)
    v8 = Vertex.ByCoordinates(0, 10, 10)

    # Create edges for bottom face
    e1 = Edge.ByStartVertexEndVertex(v1, v2)
    e2 = Edge.ByStartVertexEndVertex(v2, v3)
    e3 = Edge.ByStartVertexEndVertex(v3, v4)
    e4 = Edge.ByStartVertexEndVertex(v4, v1)

    # Create edges for top face
    e5 = Edge.ByStartVertexEndVertex(v5, v6)
    e6 = Edge.ByStartVertexEndVertex(v6, v7)
    e7 = Edge.ByStartVertexEndVertex(v7, v8)
    e8 = Edge.ByStartVertexEndVertex(v8, v5)

    # Create edges connecting bottom and top faces
    e9 = Edge.ByStartVertexEndVertex(v1, v5)
    e10 = Edge.ByStartVertexEndVertex(v2, v6)
    e11 = Edge.ByStartVertexEndVertex(v3, v7)
    e12 = Edge.ByStartVertexEndVertex(v4, v8)

    # Create wires
    w1 = Wire.ByEdges([e1, e2, e3, e4])  # bottom
    w2 = Wire.ByEdges([e5, e6, e7, e8])  # top
    w3 = Wire.ByEdges([e1, e10, e5, e9])  # front
    w4 = Wire.ByEdges([e2, e11, e6, e10])  # right
    w5 = Wire.ByEdges([e3, e12, e7, e11])  # back
    w6 = Wire.ByEdges([e4, e9, e8, e12])  # left

    # Create faces
    f1 = Face.ByExternalBoundary(w1)
    f2 = Face.ByExternalBoundary(w2)
    f3 = Face.ByExternalBoundary(w3)
    f4 = Face.ByExternalBoundary(w4)
    f5 = Face.ByExternalBoundary(w5)
    f6 = Face.ByExternalBoundary(w6)

    # Create cell
    c = Cell.ByFaces([f1, f2, f3, f4, f5, f6], 0.001)

    # Check if the cell was created with the correct type
    assert "Cell" in str(type(c))
