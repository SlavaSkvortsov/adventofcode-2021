from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Board:
    content: list[list[int]] = field(default_factory=list)

    _numbers: dict[int, tuple[int, int]] = field(default_factory=set, init=False)
    _mask: list[list[bool]] = field(default_factory=list, init=False)

    def play(self, numbers: list[int]) -> tuple[Optional[int], Optional[int]]:
        self._process()

        for turn, number in enumerate(numbers):
            result = self._cross(number)
            if result is not None:
                return turn, result

        return None, None

    def _process(self) -> None:
        self._numbers = {
            number: (row_num, col_num)
            for row_num, row in enumerate(self.content)
            for col_num, number in enumerate(row)
        }
        self._mask = [
            [False for _ in range(len(self.content[0]))]
            for _ in range(len(self.content))
        ]

    def _cross(self, number: int) -> Optional[int]:
        if number not in self._numbers:
            return None

        row_num, col_num = self._numbers[number]
        self._mask[row_num][col_num] = True
        if all(self._mask[row_num]) or all(row[col_num] for row in self._mask):
            result = sum(
                self.content[_row_num][_col_num]
                for _row_num, row in enumerate(self._mask)
                for _col_num, marked in enumerate(row)
                if not marked
            )
            return result * number

        return None


def main() -> None:
    with open('input.txt') as f:
        numbers = [int(number) for number in f.readline().split(',')]
        min_win_turn = float('+inf')
        the_best_result = 0
        board = None

        for line in f.readlines():
            if line != '\n' and board:
                board.content.append([int(number) for number in line.split()])
            else:
                if board is not None:
                    turn, result = board.play(numbers)

                    if turn is not None and turn < min_win_turn:
                        min_win_turn = turn
                        the_best_result = result

                board = Board()

        print(the_best_result)


if __name__ == '__main__':
    main()
