import dxfgrabber as grab
from dxf2shapely import polygonize_dxf
from dxf2shapely.d2s import iter_line_points
from pytest import fixture
from shapely.geometry import Polygon


@fixture
def dxf():
    return grab.readfile("test.dxf")


def test_iter_line_points(dxf):
    assert len(list(iter_line_points(dxf))) == 149


def test_polygonize_dxf(dxf):
    polygons = list(polygonize_dxf("test.dxf"))
    assert len(polygons) == 34
    assert all(type(p)==Polygon for p in polygons)