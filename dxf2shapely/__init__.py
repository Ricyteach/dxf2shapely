"""Very limited tool for grabbing line segments from pre-curated dxf files and turning them into shapely Polygons."""

__version__ = "1.1"

from .d2s import polygonize_dxf
