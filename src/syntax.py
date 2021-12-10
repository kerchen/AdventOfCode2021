from math import floor


def is_corrupt(navigation_line: str) -> bool:
    starting_delimiters = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ending_delimiters = {')': '(', ']': '[', '}': '{', '>': '<'}
    unmatched = []
    for c in navigation_line:
        if c in starting_delimiters.keys():
            unmatched.append(c)
        elif c in ending_delimiters.keys():
            if unmatched:
                if not unmatched.pop() == ending_delimiters[c]:
                    return True, c
            else:
                return True, c

    return False, ''


def get_corruption_score(character: str) -> int:
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

    return scores.get(character, 0)


def complete_line(incomplete_line: str) -> str:
    starting_delimiters = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ending_delimiters = {')': '(', ']': '[', '}': '{', '>': '<'}
    unmatched = []
    for c in incomplete_line:
        if c in starting_delimiters.keys():
            unmatched.append(c)
        elif c in ending_delimiters.keys():
            unmatched.pop()

    def map_to_closing(c):
        nonlocal starting_delimiters

        return starting_delimiters.get(c)

    unmatched = reversed(unmatched)
    completion = map(map_to_closing, unmatched)
    return ''.join(completion)


def compute_completion_score(completion: str) -> int:
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for c in completion:
        score = score * 5 + scores.get(c)

    return score


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        score = 0
        completion_scores = []
        for line in dfile:
            nav_line = line.strip()
            corrupt, stop_char = is_corrupt(nav_line)
            if corrupt:
                score += get_corruption_score(stop_char)
            else:
                completion = complete_line(nav_line)
                completion_scores.append(compute_completion_score(completion))

        print(f"Final corruption score: {score}")
        print(f"Middle completion score: {sorted(completion_scores)[floor(len(completion_scores)/2)]}")
