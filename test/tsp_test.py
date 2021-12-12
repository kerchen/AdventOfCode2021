import pytest

from tsp import CaveSystem


path_parse_test_data = [
   (["start-A",
     "A-end"],
    3),
    (["start-A",
      "A-b",
      "b-c",
      "c-D",
      "A-end"],
     6),
]


@pytest.mark.parametrize("input_data, expected_node_count", path_parse_test_data)
def test_path_input_data_parsed_correctly(input_data, expected_node_count):
    cave_system = CaveSystem(input_data)

    node_count = cave_system.node_count()
    assert node_count == expected_node_count


path_direct_connectivity_test_data = [
    (["start-A",
      "A-end"],
     'start', 'A', True),
    (["start-A",
      "A-end"],
     'end', 'A', True),
    (["start-A",
      "A-end"],
     'start', 'end', False),
    (["start-A",
      "A-b",
      "b-end"],
     'A', 'b', True),
]


@pytest.mark.parametrize("input_data, first_node, second_node, expected_directly_connected", path_direct_connectivity_test_data)
def test_direct_connectivity_of_input_nodes(input_data, first_node, second_node, expected_directly_connected):
    cave_system = CaveSystem(input_data)

    directly_connected = cave_system.are_directly_connected(first_node, second_node)
    assert directly_connected == expected_directly_connected


all_paths_test_data = [
    (["start-A",
      "A-end"],
     ["start,A,end"]),
    (["start-A",
      "A-b",
      "b-end"],
     ["start,A,b,end"]),
    (["start-A",
      "A-end",
      "start-B",
      "B-end"],
     ["start,A,end", "start,B,end"]),
    (["start-A",
      "A-end",
      "A-b"],
     ["start,A,end", "start,A,b,A,end"]),
    (["start-A",
      "start-b",
      "A-c",
      "A-b",
      "b-d",
      "A-end",
      "b-end"],
     ["start,A,b,A,c,A,end",
      "start,A,b,A,end",
      "start,A,b,end",
      "start,A,c,A,b,A,end",
      "start,A,c,A,b,end",
      "start,A,c,A,end",
      "start,A,end",
      "start,b,A,c,A,end",
      "start,b,A,end",
      "start,b,end"]),
    (["dc-end",
      "HN-start",
      "start-kj",
      "dc-start",
      "dc-HN",
      "LN-dc",
      "HN-end",
      "kj-sa",
      "kj-HN",
      "kj-dc"],
     ["start,HN,dc,HN,end",
      "start,HN,dc,HN,kj,HN,end",
      "start,HN,dc,end",
      "start,HN,dc,kj,HN,end",
      "start,HN,end",
      "start,HN,kj,HN,dc,HN,end",
      "start,HN,kj,HN,dc,end",
      "start,HN,kj,HN,end",
      "start,HN,kj,dc,HN,end",
      "start,HN,kj,dc,end",
      "start,dc,HN,end",
      "start,dc,HN,kj,HN,end",
      "start,dc,end",
      "start,dc,kj,HN,end",
      "start,kj,HN,dc,HN,end",
      "start,kj,HN,dc,end",
      "start,kj,HN,end",
      "start,kj,dc,HN,end",
      "start,kj,dc,end"]),
]


@pytest.mark.parametrize("input_data, expected_paths", all_paths_test_data)
def test_all_paths_found(input_data, expected_paths):
    cave_system = CaveSystem(input_data)

    all_paths = cave_system.find_all_paths()
    assert sorted([','.join(p) for p in all_paths]) == sorted(expected_paths)


all_paths_count_test_data = [
    (["start-A",
      "A-end"],
     1),
    (["start-A",
      "A-b",
      "b-end"],
     1),
    (["start-A",
      "A-end",
      "start-B",
      "B-end"],
     2),
    (["dc-end",
      "HN-start",
      "start-kj",
      "dc-start",
      "dc-HN",
      "LN-dc",
      "HN-end",
      "kj-sa",
      "kj-HN",
      "kj-dc"],
     19),
    (["fs-end",
      "he-DX",
      "fs-he",
      "start-DX",
      "pj-DX",
      "end-zg",
      "zg-sl",
      "zg-pj",
      "pj-he",
      "RW-he",
      "fs-DX",
      "pj-RW",
      "zg-RW",
      "start-pj",
      "he-WI",
      "zg-he",
      "pj-fs",
      "start-RW"],
     226)
 ]


@pytest.mark.parametrize("input_data, expected_path_count", all_paths_count_test_data)
def test_number_of_paths_found_is_correct(input_data, expected_path_count):
    cave_system = CaveSystem(input_data)

    all_paths = cave_system.find_all_paths()
    assert len(all_paths) == expected_path_count

