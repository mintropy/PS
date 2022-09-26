"""
Title : 2048 (Hard)
Link : https://www.acmicpc.net/problem/12094
"""

from sys import stdin

input = stdin.readline

Board = list[list[int]]


class Board:
    def __init__(self) -> None:
        self.max_value: int = 0
        self.possible: list[int] = [1]
        for _ in range(10):
            self.possible.append(self.possible[-1] * 2)

    def rotate(self, board: Board) -> list[Board]:
        board_list = [
            board,
            [line[::-1] for line in board],
            list(list(line) for line in zip(*board)),
            list(list(line) for line in zip(*[line for line in board[::-1]])),
        ]
        return board_list

    def move(self, board: Board) -> Board:
        new_board = []
        for line in board:
            new_line = [0] * len(line)
            idx = 0
            for x in line:
                if not x:
                    continue
                if not new_line[idx]:
                    new_line[idx] = x
                elif new_line[idx] == x:
                    new_line[idx] = x * 2
                    idx += 1
                else:
                    idx += 1
                    new_line[idx] = x
            new_board.append(new_line)
        return new_board

    def dfs(self, move_count: int, board: Board) -> None:
        max_value_now = max([max(line) for line in board])
        if not move_count:
            if self.max_value < max_value_now:
                self.max_value = max_value_now
            return
        if max_value_now * self.possible[move_count] <= self.max_value:
            return
        for new_board in self.rotate(board):
            if (next_board := self.move(new_board)) != board:
                self.dfs(move_count - 1, next_board)


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    board2048 = Board()
    board2048.dfs(10, board)
    print(board2048.max_value)
