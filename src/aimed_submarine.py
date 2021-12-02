from submarine import Submarine


class AimedSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, commands: list):
        for full_command in commands:
            command, amount = full_command.split()
            if command == 'forward':
                self.position += int(amount)
                self.depth += int(amount) * self.aim
            elif command == 'down':
                self.aim += int(amount)
            elif command == 'up':
                self.aim -= int(amount)
