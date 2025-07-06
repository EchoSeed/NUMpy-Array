
# EchoSeed Lattice Patch

A clean utility module to render symbolic glyph lattices using NetworkX and NumPy arrays.

## Features
- Converts glyph logs into network graphs
- Normalizes entropy into visual node size
- Handles missing/empty entropy safely
- Renders 2D lattice with spring layout

## Files
- `lattice_patch.py`: Core module
- `example_notebook.ipynb`: Colab-friendly demo
- `README.md`: This file

## Usage in Colab
```python
!wget https://raw.githubusercontent.com/YOUR_USERNAME/echoseed-tools/main/lattice_patch.py
from lattice_patch import build_lattice_graph, render_lattice
```
