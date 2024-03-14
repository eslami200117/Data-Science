import random
from collections import Counter
from typing import Generator, Any

NUM_PLAYERS = 4
BOXES = 10
WIN_BOXES = 4

class Peg:
    def __init__(self, label: str, virtual_position: int) -> None:
        self._label = label
        self._position = 0
        self._is_start = False
        self._virtual_position = virtual_position

    def __repr__(self) -> str:
        return self._label + ": " + str(self._position) + f"({self.virtual_position})"

    def start(self) -> None:
        self._is_start = True
    
    def move(self, dice: int) -> None:
        if (self._position + dice) <= (NUM_PLAYERS*BOXES + WIN_BOXES):
            self._position += dice

    def restart(self) -> None:
        self._position = 0
        self._is_start = False

    @property
    def is_start(self) -> bool:
        return self._is_start
    
    @property
    def position(self) -> int:
        return self._position
    
    @property
    def virtual_position(self) -> None:
        return self._position + self._virtual_position
    
    @property
    def label(self) -> None:
        return self._label
 

class Mensch:
    def __init__(self, num_player: int = NUM_PLAYERS, boxes: int = BOXES) -> None:
        self._num_player = num_player
        self._players = [Peg(f"Player {i+1}", boxes*i) for i in range(num_player)]
        self._current_player = self._players[0]
        self._previous_player = self._players[-1]
        self._winner = None
        self._last_box = num_player*boxes
        self._next_player = self._next_turn()

    def _roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def _next_turn(self) -> Generator[Any, None, None]:
        current_index = 1
        while True:
            yield self._players[current_index]
            current_index = (current_index + 1) % self._num_player

    def print_result(self, dice: int) -> None:
        print(self._current_player)
        print(self._players)
        print(dice)

    def _check_boxes(self) -> bool:
        if self._previous_player.position > self._last_box:
            self._winner = self._previous_player.label
            return False
        for player in self._players:
            if player is self._previous_player:
                continue
            if self._previous_player.virtual_position == player.virtual_position:
                if self._previous_player.is_start:
                    player.restart()
        return True

    def run(self) -> str:
        while self._check_boxes():
            self._previous_player = self._current_player
            dice = self._roll_dice()
            # self.print_result(dice)
            if not self._current_player.is_start:
                if dice == 6:
                    self._current_player.start()
                    continue
                self._current_player = next(self._next_player)
            else:
                self._current_player.move(dice)
                if dice == 6:
                    continue
                self._current_player = next(self._next_player)

        return self._winner


class Mensch_Simulation:
    def __init__(self, num_game: int = 10000) -> None:
        self.num_game = num_game

    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def run(self) -> int:
        game = Mensch()
        winner = game.run()
        return winner

    def simulate(self) -> Counter:
        winners = []
        for _ in range(self.num_game):
            winners.append(self.run())
        return Counter(winners)


def main():
    test = Mensch_Simulation(10000)
    result = test.simulate()
    print(result)


if __name__ == "__main__":
    main()
