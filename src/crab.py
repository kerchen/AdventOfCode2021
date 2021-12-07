from math import floor


def simple_cost(position, target):
    return abs(target - position)


def geometric_cost(position, target):
    if position == target:
        return 0
    return sum(range(abs(target - position)+1))


def compute_total_move_cost_to_position(positions: list, target_position: int, cost_func) -> int:
    total_cost = 0

    def get_cost(position: int, target: int):
        nonlocal total_cost, cost_func
        total_cost += cost_func(position, target)

    [get_cost(position, target_position) for position in positions]

    return total_cost


def find_best_meeting_point(positions: list, cost_func=simple_cost) -> tuple:
    if len(positions) < 2:
        return positions[0], 0

    min_position = min(positions)
    max_position = max(positions)

    def find_best_meeting_point_worker(positions, min_position, max_position, cost_func):
        proposed_position = min_position + floor((max_position - min_position) / 2)
        proposed_cost = compute_total_move_cost_to_position(positions, proposed_position, cost_func)

        lower_valid = False
        upper_valid = False
        if min_position == proposed_position - 1:
            best_lower_pos = min_position
            lower_half_cost = compute_total_move_cost_to_position(positions, min_position, cost_func)
            lower_valid = True
        elif min_position < proposed_position - 1:
            best_lower_pos, lower_half_cost = find_best_meeting_point_worker(positions, min_position, proposed_position - 1, cost_func)
            lower_valid = True
        if max_position == proposed_position + 1:
            best_upper_pos = max_position
            upper_half_cost = compute_total_move_cost_to_position(positions, max_position, cost_func)
            upper_valid = True
        elif max_position > proposed_position + 1:
            best_upper_pos, upper_half_cost = find_best_meeting_point_worker(positions, proposed_position + 1, max_position, cost_func)
            upper_valid = True

        if lower_valid and lower_half_cost < proposed_cost:
            proposed_cost = lower_half_cost
            proposed_position = best_lower_pos
        if upper_valid and upper_half_cost < proposed_cost:
            proposed_cost = upper_half_cost
            proposed_position = best_upper_pos

        return proposed_position, proposed_cost

    best_position, best_cost = find_best_meeting_point_worker(positions, min_position, max_position, cost_func)

    return best_position, best_cost


def solve(input_data_file: str, cost_func=simple_cost):
    with open(input_data_file, "r") as dfile:
        initial_state_str = ''
        for line in dfile:
            initial_state_str += line.strip()
        initial_state = list(map(int, initial_state_str.split(',')))
        best_position, cost = find_best_meeting_point(initial_state, cost_func)
        print(f"Best position: {best_position}  Cost: {cost}")
