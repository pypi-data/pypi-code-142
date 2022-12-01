# -*- coding: utf-8 -*-
import math
import unittest
import uuid
from io import BytesIO
from pathlib import Path

import pytest
from PIL import Image, ImageChops, ImageOps

from arkindex_worker.cache import CachedElement, create_tables, init_cache_db
from arkindex_worker.image import (
    BoundingBox,
    download_tiles,
    open_image,
    polygon_bounding_box,
    revert_orientation,
    trim_polygon,
)
from arkindex_worker.models import Element

FIXTURES = Path(__file__).absolute().parent / "data"
TILE = FIXTURES / "test_image.jpg"
FULL_IMAGE = FIXTURES / "tiled_image.jpg"
ROTATED_IMAGE = FIXTURES / "rotated_image.jpg"
MIRRORED_IMAGE = FIXTURES / "mirrored_image.jpg"
ROTATED_MIRRORED_IMAGE = FIXTURES / "rotated_mirrored_image.jpg"
TEST_IMAGE = {"width": 800, "height": 300}


def _root_mean_square(img_a, img_b):
    """
    Get the root-mean-square difference between two images for fuzzy matching
    See https://effbot.org/zone/pil-comparing-images.htm
    """
    h = ImageChops.difference(img_a, img_b).histogram()
    return math.sqrt(
        sum((value * ((idx % 256) ** 2) for idx, value in enumerate(h)))
        / float(img_a.size[0] * img_a.size[1])
    )


def test_download_tiles(responses):
    expected = Image.open(FULL_IMAGE).convert("RGB")
    with TILE.open("rb") as tile:
        tile_bytes = tile.read()

    responses.add(
        responses.GET,
        "http://nowhere/info.json",
        json={"width": 543, "height": 720, "tiles": [{"width": 181, "height": 240}]},
    )

    for x in (0, 181, 362):
        for y in (0, 240, 480):
            responses.add(
                responses.GET,
                f"http://nowhere/{x},{y},181,240/full/0/default.jpg",
                body=tile_bytes,
            )

    actual = download_tiles("http://nowhere")

    assert _root_mean_square(expected, actual) <= 5.0


def test_download_tiles_crop(responses):
    """
    Ensure download_tiles does not care about tiles that are slightly bigger than expected
    (occasional issue with the Harvard IDS image server where 1024×1024 tiles sometimes are returned as 1024x1025)
    """
    expected = Image.open(FULL_IMAGE).convert("RGB")
    tile_bytes = BytesIO()
    with TILE.open("rb") as tile:
        # Add one extra pixel to each tile to return slightly bigger tiles
        ImageOps.pad(Image.open(tile), (181, 241)).save(tile_bytes, format="jpeg")

    tile_bytes = tile_bytes.getvalue()

    responses.add(
        responses.GET,
        "http://nowhere/info.json",
        json={"width": 543, "height": 720, "tiles": [{"width": 181, "height": 240}]},
    )

    for x in (0, 181, 362):
        for y in (0, 240, 480):
            responses.add(
                responses.GET,
                f"http://nowhere/{x},{y},181,240/full/0/default.jpg",
                body=tile_bytes,
            )

    actual = download_tiles("http://nowhere")

    assert _root_mean_square(expected, actual) <= 5.0


def test_download_tiles_small(responses):
    small_tile = BytesIO()
    Image.new("RGB", (1, 1)).save(small_tile, format="jpeg")
    small_tile.seek(0)

    responses.add(
        responses.GET,
        "http://nowhere/info.json",
        json={"width": 543, "height": 720, "tiles": [{"width": 181, "height": 240}]},
    )

    responses.add(
        responses.GET,
        "http://nowhere/0,0,181,240/full/0/default.jpg",
        body=small_tile.read(),
    )

    with pytest.raises(ValueError) as e:
        download_tiles("http://nowhere")
    assert str(e.value) == "Expected size 181×240 for tile 0,0, but got 1×1"


@pytest.mark.parametrize(
    "path, is_local",
    (
        ("http://somewhere/test.jpg", False),
        ("https://somewhere/test.jpg", False),
        ("path/to/something", True),
        ("/absolute/path/to/something", True),
    ),
)
def test_open_image(path, is_local, monkeypatch):
    """Check if the path triggers a local load or a remote one"""

    monkeypatch.setattr("os.path.exists", lambda x: True)
    monkeypatch.setattr(Image, "open", lambda x: Image.new("RGB", (1, 10)))
    monkeypatch.setattr(
        "arkindex_worker.image.download_image", lambda x: Image.new("RGB", (10, 1))
    )

    image = open_image(path)

    if is_local:
        assert image.size == (1, 10)
    else:
        assert image.size == (10, 1)


@pytest.mark.parametrize(
    "rotation_angle,mirrored,expected_path",
    (
        (0, False, TILE),
        (45, False, ROTATED_IMAGE),
        (0, True, MIRRORED_IMAGE),
        (45, True, ROTATED_MIRRORED_IMAGE),
    ),
)
def test_open_image_rotate_mirror(rotation_angle, mirrored, expected_path):
    expected = Image.open(expected_path).convert("RGB")
    actual = open_image(str(TILE), rotation_angle=rotation_angle, mirrored=mirrored)
    actual.save(f"/tmp/{rotation_angle}_{mirrored}.jpg")
    assert _root_mean_square(expected, actual) <= 15.0


class TestTrimPolygon(unittest.TestCase):
    def test_trim_polygon_partially_outside_image(self):
        bad_polygon = [
            [99, 200],
            [197, 224],
            [120, 251],
            [232, 350],
            [312, 364],
            [325, 310],
            [318, 295],
            [296, 260],
            [352, 259],
            [106, 210],
            [197, 206],
            [99, 200],
        ]
        expected_polygon = [
            [99, 200],
            [197, 224],
            [120, 251],
            [232, 300],
            [312, 300],
            [325, 300],
            [318, 295],
            [296, 260],
            [352, 259],
            [106, 210],
            [197, 206],
            [99, 200],
        ]
        assert (
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])
            == expected_polygon
        )

    def test_trim_polygon_good_polygon(self):
        good_polygon = (
            (12, 56),
            (29, 60),
            (35, 61),
            (42, 59),
            (58, 57),
            (65, 61),
            (72, 57),
            (12, 56),
        )
        expected_polygon = [
            [12, 56],
            [29, 60],
            [35, 61],
            [42, 59],
            [58, 57],
            [65, 61],
            [72, 57],
            [12, 56],
        ]
        assert (
            trim_polygon(good_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])
            == expected_polygon
        )

    def test_trim_polygon_invalid_polygon(self):
        """
        An assertion error is raised the polygon input isn't a list or tuple
        """
        bad_polygon = {
            "polygon": [
                [99, 200],
                [25, 224],
                [0, 0],
                [0, 300],
                [102, 300],
                [260, 300],
                [288, 295],
                [296, 260],
                [352, 259],
                [106, 210],
                [197, 206],
                [99, 208],
            ]
        }
        with self.assertRaises(
            AssertionError, msg="Input polygon must be a valid list or tuple of points."
        ):
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])

    def test_trim_polygon_negative_coordinates(self):
        """
        Negative coordinates are ignored and replaced by 0 with no error being thrown
        """
        bad_polygon = [
            [99, 200],
            [25, 224],
            [-8, -52],
            [-12, 350],
            [102, 364],
            [260, 310],
            [288, 295],
            [296, 260],
            [352, 259],
            [106, 210],
            [197, 206],
            [99, 200],
        ]
        expected_polygon = [
            [99, 200],
            [25, 224],
            [0, 0],
            [0, 300],
            [102, 300],
            [260, 300],
            [288, 295],
            [296, 260],
            [352, 259],
            [106, 210],
            [197, 206],
            [99, 200],
        ]
        assert (
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])
            == expected_polygon
        )

    def test_trim_polygon_outside_image_error(self):
        """
        An assertion error is raised when none of the polygon's points are inside the image
        """
        bad_polygon = [
            [999, 200],
            [1097, 224],
            [1020, 251],
            [1232, 350],
            [1312, 364],
            [1325, 310],
            [1318, 295],
            [1296, 260],
            [1352, 259],
            [1006, 210],
            [997, 206],
            [999, 200],
        ]
        with self.assertRaises(
            AssertionError, msg="This polygon is entirely outside the image's bounds."
        ):
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])

    def test_trim_polygon_float_coordinates(self):
        """
        An assertion error is raised when point coordinates are not integers
        """
        bad_polygon = [
            [9.9, 200],
            [25, 224],
            [0, 0],
            [0, 300],
            [102, 300],
            [260, 300],
            [288, 295],
            [296, 260],
            [352, 259],
            [106, 210],
            [197, 206],
            [99, 20.8],
        ]
        with self.assertRaises(
            AssertionError, msg="Polygon point coordinates must be integers."
        ):
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])

    def test_trim_polygon_invalid_points_1(self):
        """
        An assertion error is raised when point coordinates are not lists or tuples
        """
        bad_polygon = [
            [12, 56],
            [29, 60],
            [35, 61],
            "[42, 59]",
            [58, 57],
            [65, 61],
            [72, 57],
            [12, 56],
        ]
        with self.assertRaises(
            AssertionError, msg="Polygon points must be tuples or lists."
        ):
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])

    def test_trim_polygon_invalid_points_2(self):
        """
        An assertion error is raised when point coordinates are not lists or tuples of length 2
        """
        bad_polygon = [
            [12, 56],
            [29, 60, 3],
            [35, 61],
            [42, 59],
            [58, 57],
            [65, 61],
            [72, 57],
            [12, 56],
        ]
        with self.assertRaises(
            AssertionError, msg="Polygon points must be tuples or lists of 2 elements."
        ):
            trim_polygon(bad_polygon, TEST_IMAGE["width"], TEST_IMAGE["height"])


@pytest.mark.parametrize(
    "angle, mirrored, updated_bounds, reverse",
    (
        (
            0,
            False,
            {"x": 295, "y": 11, "width": 111, "height": 47},  # upper right
            True,
        ),
        (
            90,
            False,
            {"x": 510, "y": 295, "width": 47, "height": 111},  # lower right
            True,
        ),
        (
            180,
            False,
            {"x": 9, "y": 510, "width": 111, "height": 47},  # lower left
            True,
        ),
        (
            270,
            False,
            {"x": 11, "y": 9, "width": 47, "height": 111},  # upper left
            True,
        ),
        (
            0,
            True,
            {"x": 9, "y": 11, "width": 111, "height": 47},  # upper left
            True,
        ),
        (
            90,
            True,
            {"x": 510, "y": 9, "width": 47, "height": 111},  # upper right
            True,
        ),
        (
            180,
            True,
            {"x": 295, "y": 510, "width": 111, "height": 47},  # lower right
            True,
        ),
        (
            270,
            True,
            {"x": 11, "y": 295, "width": 47, "height": 111},  # lower left
            True,
        ),
        (
            0,
            False,
            {"x": 295, "y": 11, "width": 111, "height": 47},  # upper right
            False,
        ),
        (
            90,
            False,
            {"x": 11, "y": 162, "width": 47, "height": 111},  # upper left
            False,
        ),
        (
            180,
            False,
            {"x": 9, "y": 510, "width": 111, "height": 47},  # lower left
            False,
        ),
        (
            270,
            False,
            {"x": 357, "y": 295, "width": 47, "height": 111},  # lower right
            False,
        ),
        (
            0,
            True,
            {"x": 9, "y": 11, "width": 111, "height": 47},  # upper left
            False,
        ),
        (
            90,
            True,
            {"x": 357, "y": 162, "width": 47, "height": 111},  # lower left
            False,
        ),
        (
            180,
            True,
            {"x": 295, "y": 510, "width": 111, "height": 47},  # lower right
            False,
        ),
        (
            270,
            True,
            {"x": 11, "y": 295, "width": 47, "height": 111},  # upper right
            False,
        ),
    ),
)
def test_revert_orientation(angle, mirrored, updated_bounds, reverse, tmp_path):
    """Test cases, for both Elements and CachedElements:
    - no rotation or orientation
    - rotation with 3 different angles (90, 180, 270)
    - rotation + mirror with 4 angles (0, 90, 180, 270)
    """
    child_polygon = [[295, 11], [295, 58], [406, 58], [406, 11], [295, 11]]

    # Setup cache db to test with CachedElements
    db_path = f"{tmp_path}/db.sqlite"
    init_cache_db(db_path)
    create_tables()

    image_polygon = [
        [0, 0],
        [0, 568],
        [415, 568],
        [415, 0],
        [0, 0],
    ]
    element = Element(
        {
            "mirrored": mirrored,
            "rotation_angle": angle,
            "zone": {"polygon": image_polygon},
        }
    )
    cached_element = CachedElement.create(
        id=uuid.uuid4(),
        type="paragraph",
        polygon=image_polygon,
        mirrored=mirrored,
        rotation_angle=angle,
    )

    assert polygon_bounding_box(
        revert_orientation(element, child_polygon, reverse=reverse)
    ) == BoundingBox(**updated_bounds)

    assert polygon_bounding_box(
        revert_orientation(cached_element, child_polygon, reverse=reverse)
    ) == BoundingBox(**updated_bounds)
