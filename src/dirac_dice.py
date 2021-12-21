

class DeterministicDie:
    def __init__(self, sides=100):
        self.next_roll = 0
        self.roll_count = 0
        self.sides = sides

    def roll(self) -> int:
        self.roll_count += 1
        this_roll = self.next_roll + 1
        self.next_roll = this_roll % self.sides
        return this_roll


class DiracDiceGame:
    def __init__(self, starting_positions: list[int], target_score: int=1000):
        self.player_positions = starting_positions
        self.player_scores = [0] * len(starting_positions)
        self.die = DeterministicDie()
        self.target_score = target_score

    def score(self, player: int) -> int:
        return self.player_scores[player-1]

    def play_turns(self, turn_count) -> bool:
        for t in range(turn_count):
            for i, p in enumerate(self.player_positions):
                for r in range(3):
                    p += self.die.roll()
                self.player_positions[i] = ((p - 1) % 10) + 1
                self.player_scores[i] += self.player_positions[i]
                if self.player_scores[i] >= self.target_score:
                    return True

        return False


def solve(starting_positions: list[int], target_score):
    game = DiracDiceGame(starting_positions, target_score)
    while True:
        if game.play_turns(1):
            break
    print(f"Game ended with p1 score {game.player_scores[0]} p2 score {game.player_scores[1]}")
    losing_score = min(game.player_scores)
    print(f"Losing score {losing_score}   # of dice rolls {game.die.roll_count}")
    print(f"Product: {losing_score * game.die.roll_count}")
