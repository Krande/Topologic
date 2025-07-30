# Topologic Python Tests

This directory contains pytest tests for the Topologic Python bindings.

## Running Tests

Tests can be run using the `pytest` command:

```bash
pytest
```

Or using the pixi task:

```bash
pixi run test
```

## Test Structure

- `conftest.py` - Sets up the path to the Topologic library
- `test_vertex.py` - Tests for Vertex functionality
- `test_edge_wire.py` - Tests for Edge and Wire functionality
- `test_face_cell.py` - Tests for Face and Cell functionality
- `test_cell_complex.py` - Tests for CellComplex functionality
- `test_dictionary.py` - Tests for Dictionary and Attribute functionality

## Notes

These tests assume that the Topologic library has been built and installed. The tests look for the library in `~/topologicbim/Topologic/output/x64/Release`. If your library is in a different location, you may need to modify the `conftest.py` file.
