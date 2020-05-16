import ezdxf
import shapely.ops
import shapely.geometry


def iter_line_coord_pairs(space):
    dxf_lines = list(e for e in space if e.dxftype() == 'LINE')
    yield from ([
            list(
                round(c, 3) for c in l.dxf.start[:-1]
            ),
            list(
                round(c, 3) for c in l.dxf.end[:-1]
            )
        ] for l in dxf_lines)


def polygonize_dxf(f):
    doc = ezdxf.readfile(f)
    msp = doc.modelspace()
    coord_pairs = iter_line_coord_pairs(msp)
    return shapely.ops.polygonize(coord_pairs)
