import pytest

from polymer import parse_input, perform_insertions, compute_component_counts


input_parse_test_data = [
    ('''NNCB

CH -> B
HH -> N
CB -> H
CN -> C''',
     'NNCB',
     {('C', 'H'): 'B', ('H', 'H'): 'N', ('C', 'B'): 'H', ('C', 'N'): 'C'}
     ),
]


@pytest.mark.parametrize("input_data, expected_start_sequence, expected_insertions", input_parse_test_data)
def test_input_data_parsed_correctly(input_data, expected_start_sequence, expected_insertions):
    start_sequence, insertions = parse_input(input_data)
    assert start_sequence == expected_start_sequence
    assert insertions == expected_insertions


insertion_test_data = [
    ('''NNCB

NN -> B''',
     'NBNCB'
     ),

    ('''NNCB

NN -> B
CB -> G''',
     'NBNCGB'
     ),

    ('''NNCB

NN -> B
CB -> G
NC -> F''',
     'NBNFCGB'
     ),

    ('''NBNFCGB

NB -> B
BN -> B
NF -> F
FC -> C
CG -> B
GB -> B''',
     'NBBBNFFCCBGBB'
     ),

    ('''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C''',
     'NCNBCHB'
     ),
]


@pytest.mark.parametrize("input_data, expected_sequence", insertion_test_data)
def test_insertions_handled_correctly(input_data, expected_sequence):
    start_sequence, insertions = parse_input(input_data)
    computed_sequence = perform_insertions(start_sequence, insertions)
    assert computed_sequence == expected_sequence


example_input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

multiple_rounds_test_data = [
    (example_input,
     1, 'NCNBCHB'
     ),

    (example_input,
     2, 'NBCCNBBBCBHCB'
     ),

    (example_input,
     3, 'NBBBCNCCNBBNBNBBCHBHHBCHB'
     ),

    (example_input,
     4, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
     ),
]


@pytest.mark.parametrize("input_data, step_count, expected_sequence", multiple_rounds_test_data)
def test_multiple_rounds_of_insertions_produce_correct_sequence(input_data, step_count, expected_sequence):
    start_sequence, insertions = parse_input(input_data)
    for r in range(step_count):
        computed_sequence = perform_insertions(start_sequence, insertions)
        start_sequence = computed_sequence

    assert computed_sequence == expected_sequence


count_test_data = [
    ('ABCD', {'A': 1, 'B': 1, 'C': 1, 'D': 1}),
    ('AAAD', {'A': 3, 'D': 1}),

]


@pytest.mark.parametrize("input_data, expected_counts", count_test_data)
def test_multiple_rounds_of_insertions_produce_correct_sequence(input_data, expected_counts):
    counts = compute_component_counts(input_data)

    assert counts == expected_counts


multiple_rounds_element_count_test_data = [
    (example_input,
     1, {'B': 2, 'C': 2, 'H': 1, 'N': 2}
     ),

    (example_input,
     2, {'B': 6, 'C': 4, 'H': 1, 'N': 2}
     ),

    (example_input,
     3, {'B': 11, 'C': 5, 'H': 4, 'N': 5}
     ),

    (example_input,
     4, {'B': 23, 'C': 10, 'H': 5, 'N': 11}
     ),

    (example_input,
     10, {'B': 1749, 'C': 298, 'H': 161, 'N': 865 }
     ),

]


@pytest.mark.parametrize("input_data, step_count, expected_counts", multiple_rounds_element_count_test_data)
def test_multiple_rounds_of_insertions_produce_correct_counts(input_data, step_count, expected_counts):
    start_sequence, insertions = parse_input(input_data)
    for r in range(step_count):
        computed_sequence = perform_insertions(start_sequence, insertions)
        start_sequence = computed_sequence

    counts = compute_component_counts(computed_sequence)
    assert counts == expected_counts

