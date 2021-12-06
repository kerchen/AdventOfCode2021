

class Lanternfish:
    def __init__(self, initial_timer_value: int):
        self.timer = initial_timer_value

    def advance_age(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
