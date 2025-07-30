import pytest
import sys

def test_vertex_creation():
    """Test creation of a Vertex by coordinates."""
    from topologic_core import Vertex

    # Create a vertex with specific coordinates
    v = Vertex.ByCoordinates(10, 20, 30)

    # Check if the vertex was created with the correct type
    assert str(type(v)) == "<class 'topologic_core.Vertex'>"

    # Check if coordinates are correct
    assert v.X() == 10
    assert v.Y() == 20
    assert v.Z() == 30

def test_vertex_edges():
    """Test retrieving edges from a vertex."""
    from topologic_core import Vertex, Edge

    # Create vertices
    v1 = Vertex.ByCoordinates(0, 0, 0)
    v2 = Vertex.ByCoordinates(10, 0, 0)
    v3 = Vertex.ByCoordinates(0, 10, 0)

    # Create edges connected to v1
    e1 = Edge.ByStartVertexEndVertex(v1, v2)
    e2 = Edge.ByStartVertexEndVertex(v1, v3)

    # Create a cluster to serve as the host topology
    from topologic_core import Cluster
    cluster = Cluster.ByTopologies([e1, e2])

    # Get edges from v1
    edges = []
    v1.Edges(cluster, edges)

    # Check if we got the expected number of edges
    assert len(edges) == 2

    # Check if these are indeed edges
    for edge in edges:
        assert "Edge" in str(type(edge))
