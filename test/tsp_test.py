import pytest

from tsp import CaveSystem


path_parse_test_data = [
   (["start-A",
     "A-end"],
    3),
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
