import dxfgrabber as grab
from dxfgrabber.dxfentities import Line
from shapely.ops import polygonize


def iter_line_points(dxf):
    entities = dxf.entities
    lines = (e for e in entities if isinstance(e, Line))
    yield from ((l.start[:-1], l.end[:-1]) for l in lines)


def polygonize_dxf(f):
    dxf = grab.readfile(f)
    iline_points = iter_line_points(dxf)
    return polygonize(iline_points)