

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


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        score = 0
        for line in dfile:
            corrupt, stop_char = is_corrupt(line.strip())
            if corrupt:
                score += get_corruption_score(stop_char)

        print(f"Final corruption score: {score}")
