"""
Title : ⚾
Link : https://www.acmicpc.net/problem/17281
"""

from itertools import permutations
from sys import stdin

input = stdin.readline


def make_turn(turn: tuple[int]) -> list[int]:
    turn = list(turn[:3]) + [0] + list(turn[3:])
    return turn


def simulate(N: int, hitters: list[list[int]], turn: list[int]) -> int:
    idx = score = 0
    for inning in range(N):
        out = 0
        first = second = third = 0
        while out < 3:
            hitter = turn[idx]
            point = hitters[inning][hitter]
            if point == 0:
                out += 1
            elif point == 1:
                score += third
                first, second, third = 1, first, second
            elif point == 2:
                score += second + third
                first, second, third = 0, 1, first
            elif point == 3:
                score += first + second + third
                first, second, third = 0, 0, 1
            elif point == 4:
                score += 1 + first + second + third
                first = second = third = 0
            idx = (idx + 1) % 9
    return score


if __name__ == "__main__":
    N = int(input())
    hitters = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for perm in permutations(range(1, 9), 8):
        score = simulate(N, hitters, make_turn(perm))
        if max_score < score:
            max_score = score
    print(max_score)
