def test_edge_creation():
    """Test creation of an Edge from two vertices."""
    from topologic_core import Vertex, Edge

    # Create vertices
    v1 = Vertex.ByCoordinates(0, 0, 0)
    v2 = Vertex.ByCoordinates(10, 0, 0)

    # Create edge
    e = Edge.ByStartVertexEndVertex(v1, v2)

    # Check if the edge was created with the correct type
    assert "Edge" in str(type(e))

    # Retrieve vertices from edge
    vertices = []
    e.Vertices(e, vertices)

    # Check if we got the expected number of vertices
    assert len(vertices) == 2

    # Check if these are indeed vertices with correct coordinates
    assert vertices[0].X() == 0 and vertices[0].Y() == 0 and vertices[0].Z() == 0
    assert vertices[1].X() == 10 and vertices[1].Y() == 0 and vertices[1].Z() == 0

def test_wire_creation():
    """Test creation of a Wire from edges."""
    from topologic_core import Vertex, Edge, Wire

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

    # Check if the wire was created with the correct type
    assert "Wire" in str(type(w))

    # Retrieve edges from wire
    edges = []
    w.Edges(w, edges)

    # Check if we got the expected number of edges
    assert len(edges) == 4

    # Retrieve vertices from wire
    vertices = []
    w.Vertices(w, vertices)

    # Check if we got the expected number of vertices
    assert len(vertices) == 4
