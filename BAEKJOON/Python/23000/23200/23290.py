"""
Title : 마법사 상어와 복제
Link : https://www.acmicpc.net/problem/23290
"""

from collections import deque
from dataclasses import dataclass
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

delta: tuple[tuple[int]] = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)


@dataclass
class Fish:
    d: int

    def move(self, x: int, y: int) -> tuple[int]:
        for _ in range(8):
            nx, ny = x + delta[self.d][0], y + delta[self.d][1]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                d = (d - 1) % 8
                continue
            return (nx, ny)
        return (x, y)


def solution(
    N: int, S: int, fishes: dict[tuple[int], list[Fish]], sx: int, sy: int
) -> int:
    odor = deque([[], []])
    for _ in range(S):
        copied_fishes = fishes
        new_fishes = {(i, j): [] for i in range(4) for j in range(4)}
        for fish in sum(fishes.values(), []):
            pass


def move_fishes():
    pass


if __name__ == "__main__":
    M, S = MIIS()
    fishes = {(i, j): [] for i in range(4) for j in range(4)}
    for _ in range(M):
        x, y, d = MIIS()
        fishes[(x, y)].append(Fish(d))
    sx, sy = MIIS()
