
class Submarine:
    def __init__(self):
        self.position = 0

    def move(self, commands: list):
        for full_command in commands:
            command, amount = full_command.split()
            if command == 'forward':
                self.position += int(amount)

