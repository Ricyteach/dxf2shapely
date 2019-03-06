# dxf2shapely
Very limited tool for grabbing line segments from pre-curated dxf files and turning them into shapely Polygons.

```python
from dxf2shapely import polygonize_dxf
import shapely.geometry.Polygon

polygons = polygonize_dxf('some_file.dxf')
assert all(type(p)==shapely.geometry.Polygon for p in polygons) 
```