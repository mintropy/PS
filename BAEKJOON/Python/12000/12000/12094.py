"""
Title : 2048 (Hard)
Link : https://www.acmicpc.net/problem/12094
"""

from sys import stdin

input = stdin.readline

Board = list[list[int]]


def dfs(max_value: int, move_count: int, board: Board, possible: list[int]) -> int:
    if not move_count:
        return max_value
    for i in range(4):
        new_board = [line[::] for line in board]
        max_value_next, new_board = move(new_board, i)
        if new_board == board:
            continue
        if max_value < (
            possible_max_value := dfs(
                max_value_next, move_count - 1, new_board, possible
            )
        ):
            max_value = possible_max_value
    return max_value


def move(board: Board, d: int) -> tuple[int, Board]:
    max_value = 0
    if d == 0:
        for j in range(N):
            idx = prev = 0
            for i in range(N):
                if x := board[i][j]:
                    if prev == x:
                        max_value = max(x, prev * 2)
                        board[idx - 1][j] = prev * 2
                        board[i][j] = 0
                        prev = 0
                    else:
                        max_value = max(x, prev)
                        prev = board[i][j]
                        board[i][j] = 0
                        board[idx][j] = prev
                        idx += 1
    elif d == 1:
        for i in range(N):
            idx = N - 1
            prev = 0
            for j in range(N - 1, -1, -1):
                if x := board[i][j]:
                    if prev == x:
                        max_value = max(x, prev * 2)
                        board[i][idx + 1] = prev * 2
                        board[i][j] = 0
                        prev = 0
                    else:
                        max_value = max(x, prev)
                        prev = board[i][j]
                        board[i][j] = 0
                        board[i][idx] = prev
                        idx -= 1
    elif d == 2:
        for j in range(N):
            idx = N - 1
            prev = 0
            for i in range(N - 1, -1, -1):
                if x := board[i][j]:
                    if prev == x:
                        max_value = max(x, prev * 2)
                        board[idx + 1][j] = prev * 2
                        board[i][j] = 0
                        prev = 0
                    else:
                        max_value = max(x, prev)
                        prev = board[i][j]
                        board[i][j] = 0
                        board[idx][j] = prev
                        idx -= 1
    elif d == 3:
        for j in range(N):
            idx = prev = 0
            for i in range(N):
                if x := board[i][j]:
                    if prev == x:
                        max_value = max(x, prev * 2)
                        board[i][idx - 1] = prev * 2
                        board[i][j] = 0
                        prev = 0
                    else:
                        max_value = max(x, prev)
                        prev = board[i][j]
                        board[i][j] = 0
                        board[i][idx] = prev
                        idx += 1
    return max_value, board


if __name__ == "__main__":
    N: int = int(input())
    board: Board = [list(map(int, input().split())) for _ in range(N)]
    max_value: int = max([max(line) for line in board])
    possible: list[int] = [1]
    for _ in range(10):
        possible.append(possible[-1] * 2)
    print(dfs(max_value, 10, board, possible))
