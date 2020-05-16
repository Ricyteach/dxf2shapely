import ezdxf
from dxf2shapely import polygonize_dxf
from dxf2shapely.d2s import iter_line_coord_pairs
from pytest import fixture
from shapely.geometry import Polygon


@fixture
def msp():
    doc = ezdxf.readfile("test.dxf")
    return doc.modelspace()


def test_iter_line_points(msp):
    assert len(list(iter_line_coord_pairs(msp))) == 149


def test_polygonize_dxf(msp):
    polygons = list(polygonize_dxf("test.dxf"))
    assert len(polygons) == 34
    assert all(type(p)==Polygon for p in polygons)