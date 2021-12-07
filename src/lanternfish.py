

class Lanternfish:
    def __init__(self, initial_timer_value: int):
        self.timer = initial_timer_value
        self.representation_count = 1

    def advance_age(self) -> bool:
        spawned = False
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            spawned = True
        return spawned


def simulate_fish(initial_state: list, days: int, enumerate_fish: bool = True):
    population = []
    for initial_timer_value in initial_state:
        population.append(Lanternfish(initial_timer_value))

    for day in range(days):
        spawn_count = 0

        def age_fish(fish: Lanternfish):
            nonlocal spawn_count
            if fish.advance_age():
                spawn_count += fish.representation_count

        [age_fish(fish) for fish in population]

        if spawn_count:
            representative_fish = Lanternfish(8)
            representative_fish.representation_count = spawn_count
            population.append(representative_fish)

    if enumerate_fish:
        return_list = []
        for fish in population:
            return_list.extend([fish.timer] * fish.representation_count)

        return return_list
    else:
        fish_count = 0
        for fish in population:
            fish_count += fish.representation_count
        return fish_count


def solve(input_data_file: str, days: int):
    with open(input_data_file, "r") as dfile:
        initial_state_str = ''
        for line in dfile:
            initial_state_str += line.strip()
        initial_state = initial_state_str.split(',')
        if days < 20:
            final_state = simulate_fish(list(map(int, initial_state)), days, True)
            print("Final state: " + str(final_state))
            print(f"Fish count: {len(final_state)}")
        else:
            final_count = simulate_fish(list(map(int, initial_state)), days, False)
            print(f"Fish count: {final_count}")
