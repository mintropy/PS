"""
Title : 마법사 상어와 복제
Link : https://www.acmicpc.net/problem/23290
"""

from collections import deque
from dataclasses import dataclass
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

delta_fish: tuple[tuple[int]] = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)
delta_shark: tuple[tuple[int]] = ((-1, 0), (0, -1), (1, 0), (0, 1))


@dataclass
class Fish:
    d: int

    def move(self, x: int, y: int) -> tuple[int]:
        for _ in range(8):
            nx, ny = x + delta_fish[self.d][0], y + delta_fish[self.d][1]
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
        for (x, y), fish_list in fishes.items():
            for fish in fish_list:
                nx, ny = fish.move(x, y)
                new_fishes[(nx, ny)].append(fish)
        sx, sy, new_oder = move_shark(sx, sy)
        remove_odor()
        fishes += new_fishes + copied_fishes


def move_shark(sx: int, sy: int):
    odor = []
    for _ in range(3):
        d = max_fish = 0
        for i, (dx, dy) in enumerate(delta_shark):
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                if max_fish < (f := len(fishes[(nx, ny)])):
                    max_fish = f
                    d = i
        odor.append((sx, sy))
        sx, sy = sx + delta_shark[d][0], sy + delta_shark[d][1]
    return sx, sy, odor


def remove_odor(odor: list[tuple[int]]):
    for x, y in odor:
        pass


if __name__ == "__main__":
    M, S = MIIS()
    fishes = {(i, j): [] for i in range(4) for j in range(4)}
    for _ in range(M):
        x, y, d = MIIS()
        fishes[(x, y)].append(Fish(d))
    sx, sy = MIIS()
