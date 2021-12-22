from datetime import datetime
from math import pow, log10, floor

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


class ConstantDie:
    def __init__(self, value: int):
        self.value = value
        self.roll_count = 0

    def roll(self) -> int:
        self.roll_count += 1
        return self.value


class DiracDie:
    def __init__(self, max_depth, depth: int):
        self.depth = depth
        self.max_depth = max_depth
        if depth < max_depth:
            self.subdie = DiracDie(max_depth, depth+1)
        else:
            self.subdie = None
        self.next_roll = 1

    def is_exhausted(self):
        if not self.subdie:
            return self.next_roll == 1

        return self.next_roll == 1 and self.subdie.is_exhausted()

    def next_universe(self, prune_depth: int) -> bool:
        if self.depth > prune_depth:
            self.next_roll = 1
            if self.subdie:
                self.subdie.next_universe(prune_depth)
            return True
        subdie_pruned = False
        if self.subdie:
            subdie_pruned = self.subdie.next_universe(prune_depth)
        if self.depth == prune_depth or subdie_pruned:
            self.next_roll += 1
            if self.next_roll > 3:
                self.next_roll = 1
                return True
        return False

    def roll(self, roll_number) -> int:
        if self.depth == roll_number:
            return self.next_roll
        if not self.subdie:
            raise Exception(f"uh oh! Need more than {roll_number} roll depth")
        return self.subdie.roll(roll_number)


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


class MultiverseDiracDiceGame:
    def __init__(self, starting_positions: list[int], target_score: int, die: DiracDie):
        self.player_positions = starting_positions
        self.player_scores = [0] * len(starting_positions)
        self.die = die
        self.target_score = target_score
        self.total_rolls = 0

    def score(self, player: int) -> int:
        return self.player_scores[player-1]

    def play_turn(self) -> tuple:
        for i, p in enumerate(self.player_positions):
            for r in range(3):
                self.total_rolls += 1
                p += self.die.roll(self.total_rolls)
            self.player_positions[i] = ((p - 1) % 10) + 1
            self.player_scores[i] += self.player_positions[i]
            if self.player_scores[i] >= self.target_score:
                self.die.next_universe(self.total_rolls)
                return True, i

        return False, 0


def solve(starting_positions: list[int], target_score, die):
    game = DiracDiceGame(starting_positions, target_score)
    game.die = die
    while True:
        if game.play_turns(1):
            break
    print(f"Game ended with p1 score {game.player_scores[0]} p2 score {game.player_scores[1]}")
    losing_score = min(game.player_scores)
    print(f"Losing score {losing_score}   # of dice rolls {game.die.roll_count}")
    print(f"Product: {losing_score * game.die.roll_count}")


def solve_p2(starting_positions: list[int], max_rolls, target_score):
    dd = DiracDie(max_rolls, 1)
    game = MultiverseDiracDiceGame(starting_positions, target_score, dd)
    p1_wins = 0
    p2_wins = 0
    start_time = datetime.now()
    games_played = 0
    game_limit = pow(3, max_rolls)
    perf_markers = [x for x in range(1, floor(log10(game_limit)))]
    while games_played < game_limit:
        won, winner = game.play_turn()
        if won:
            games_played += 1
            if winner == 0:
                p1_wins += 1
            else:
                p2_wins += 1

            for n in perf_markers:
                marker = int(pow(10, n))
                if games_played == marker:
                    dt = datetime.now() - start_time
                    elapsed_seconds = dt.total_seconds()
                    if elapsed_seconds == 0:
                        elapsed_seconds = 0.0001
                    rate = marker / elapsed_seconds
                    ttc = rate / game_limit
                    print(f"{games_played} games played at {datetime.now() - start_time}; rate = {rate} games/sec")
                    print(f"Est. time to completion: {ttc} sec")

            dd = game.die
            if dd.is_exhausted():
                break
            game = MultiverseDiracDiceGame(starting_positions, target_score, dd)

    print(f"Player 1 wins: {p1_wins}\nPlayer 2 wins: {p2_wins}")


if __name__ == "__main__":
    solve_p2([4, 8], 40, 21)
