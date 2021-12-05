import pytest

from vent_field import PlumeLine, Point, VentField

parse_line_start_test_data = [
    ("0,0 -> 0,1", Point(0, 0)),
    ("2,3 -> 0,1", Point(2, 3)),
    ("11,93 -> 0,1", Point(11, 93))
]


@pytest.mark.parametrize("line_points, expected_start", parse_line_start_test_data)
def test_line_data_parsing_start_point(line_points, expected_start):
    plume_line = PlumeLine(line_points)
    assert plume_line.start == expected_start


parse_line_end_test_data = [
    ("0,0 -> 0,1", Point(0, 1)),
    ("0,0 -> 2,3", Point(2, 3)),
    ("0,0 -> 11,93", Point(11, 93))
]


@pytest.mark.parametrize("line_points, expected_end", parse_line_end_test_data)
def test_line_data_parsing_end_point(line_points, expected_end):
    plume_line = PlumeLine(line_points)
    assert plume_line.end == expected_end


vent_field_axial_overlapping_test_data = [
    (["0,0 -> 0,1"], 0),
    (["0,0 -> 0,1",
      "1,0 -> 1,2"], 0),
    (["0,0 -> 0,1",
      "0,1 -> 2,1"], 1),
    (["0,0 -> 0,1",
      "0,0 -> 0,1",
      "0,0 -> 0,1",
      "0,0 -> 0,1"], 2),
    (["0,0 -> 0,1",
      "0,0 -> 0,2",
      "0,0 -> 0,3",
      "0,0 -> 0,4"], 4),
    (["0,9 -> 5,9",
      "8,0 -> 0,8",
      "9,4 -> 3,4",
      "2,2 -> 2,1",
      "7,0 -> 7,4",
      "6,4 -> 2,0",
      "0,9 -> 2,9",
      "3,4 -> 1,4",
      "0,0 -> 8,8",
      "5,5 -> 8,2"], 5),
]


@pytest.mark.parametrize("vent_field_lines, expected_overlap_count", vent_field_axial_overlapping_test_data)
def test_vent_field_axial_overlapping_count(vent_field_lines, expected_overlap_count):
    vent_field = VentField(vent_field_lines)
    overlap_count = vent_field.get_overlap_count()
    assert overlap_count == expected_overlap_count

