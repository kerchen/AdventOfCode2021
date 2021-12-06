

class Lanternfish:
    def __init__(self, initial_timer_value: int):
        self.timer = initial_timer_value

    def advance_age(self) -> bool:
        spawned = False
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            spawned = True
        return spawned


def simulate_fish(initial_state: list, days: int):
    population = []
    for initial_timer_value in initial_state:
        population.append(Lanternfish(initial_timer_value))

    for day in range(days):
        spawn_count = 0

        def age_fish(fish: Lanternfish):
            nonlocal spawn_count
            if fish.advance_age():
                spawn_count += 1

        [age_fish(fish) for fish in population]

        while spawn_count > 0:
            population.append(Lanternfish(8))
            spawn_count -= 1

    return [fish.timer for fish in population]
