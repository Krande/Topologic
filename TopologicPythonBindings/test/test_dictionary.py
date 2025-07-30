import pytest

def test_dictionary():
    """Test creating and using a Dictionary with various attribute types."""
    from topologic_core import Vertex, Dictionary, IntAttribute, DoubleAttribute, StringAttribute

    # Create attributes with different types
    i = 340
    d = 120.567
    s = "Hello Topologic World"

    int_attr = IntAttribute(i)
    double_attr = DoubleAttribute(d)
    string_attr = StringAttribute(s)

    # Check attribute values
    assert int_attr.IntValue() == i
    assert double_attr.DoubleValue() == d
    assert string_attr.StringValue() == s

    # Create dictionary
    keys = ["int", "double", "string"]
    values = [int_attr, double_attr, string_attr]
    my_dict = Dictionary.ByKeysValues(keys, values)

    # Create a vertex and set the dictionary
    v = Vertex.ByCoordinates(0, 0, 0)
    v.SetDictionary(my_dict)

    # Retrieve dictionary from vertex
    retrieved_dict = v.GetDictionary()

    # Retrieve attributes from retrieved dictionary
    retrieved_int_attr = retrieved_dict.ValueAtKey(keys[0])
    retrieved_double_attr = retrieved_dict.ValueAtKey(keys[1])
    retrieved_string_attr = retrieved_dict.ValueAtKey(keys[2])

    # Check if retrieved values match original values
    assert retrieved_int_attr.IntValue() == i
    assert retrieved_double_attr.DoubleValue() == d
    assert retrieved_string_attr.StringValue() == s
