""" Geometric shapes and operations on them
"""

from ._base import (
    Coordinate,
    BoundingBox,
    CRSProjProxy,
    InvalidCRSError,
    CRS,
    Geometry,
    GeoBox,
    point,
    multipoint,
    line,
    multiline,
    polygon,
    multipolygon,
    box,
    polygon_from_transform,
    unary_union,
    unary_intersection,
)

from .tools import (
    roi_is_empty,
    roi_shape,
    scaled_down_geobox,
    scaled_down_shape,
    scaled_down_roi,
    scaled_up_roi,
    decompose_rws,
    affine_from_pts,
    get_scale_at_point,
)

__all__ = [
    "Coordinate",
    "BoundingBox",
    "CRSProjProxy",
    "InvalidCRSError",
    "CRS",
    "Geometry",
    "GeoBox",
    "point",
    "multipoint",
    "line",
    "multiline",
    "polygon",
    "multipolygon",
    "box",
    "polygon_from_transform",
    "unary_union",
    "unary_intersection",
    "roi_is_empty",
    "roi_shape",
    "scaled_down_geobox",
    "scaled_down_shape",
    "scaled_down_roi",
    "scaled_up_roi",
    "decompose_rws",
    "affine_from_pts",
    "get_scale_at_point",
]