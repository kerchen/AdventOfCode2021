from collections import Counter


def parse_input(input_data: str) -> tuple:
    lines = input_data.split('\n')
    sequence_start = lines[0].strip()
    insertions = dict()

    for line in lines[2:]:
        split_line = line.strip().split(' -> ')
        insertions[(split_line[0][0], split_line[0][1])] = split_line[1]

    return sequence_start, insertions


def perform_insertions(start_sequence: list, insertions: dict) -> list:
    new_sequence = ''
    for i, c in enumerate(start_sequence):
        new_sequence = new_sequence + c
        if i == len(start_sequence) - 1:
            break
        seq_pair = (c, start_sequence[i+1])
        if seq_pair in insertions.keys():
            new_sequence = new_sequence + insertions[seq_pair]

    return new_sequence


def compute_component_counts(sequence: str) -> dict:
    return Counter(sequence)


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        start_sequence, insertions = parse_input(dfile.read())

        computed_sequence = start_sequence
        for r in range(10):
            computed_sequence = perform_insertions(computed_sequence, insertions)
        counts = compute_component_counts(computed_sequence)
        min_count = len(computed_sequence)
        max_count = 0
        for k, v in counts.items():
            if v < min_count:
                min_count = v
            if v > max_count:
                max_count = v

        print(f"After 10 insertions: max and min are {max_count} and {min_count}")
        print(f"and their difference is {max_count - min_count}")
