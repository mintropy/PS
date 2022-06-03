"""
Title : 괄호 추가하기2
Link : https://www.acmicpc.net/problem/16638
"""

from itertools import combinations
from sys import stdin

input = stdin.readline


def check_brackets(pos: tuple) -> bool:
    for i in range(len(pos) - 1):
        if pos[i + 1] - pos[i] == 1:
            return False
    return True


def make_poly(poly: list, pos: tuple) -> str:
    for x in pos[::-1]:
        poly = f"{poly[:x * 2]}({poly[x * 2:(x + 1) * 2 + 1]}){poly[(x + 1) * 2 + 1:]}"
    return poly


if __name__ == "__main__":
    N = int(input())
    poly = input().strip()
    max_value = eval(poly)
    for i in range(1, N // 2 + 1):
        comb = combinations(range(N // 2), i)
        for pos in comb:
            if not check_brackets(pos):
                continue
            max_value = max(max_value, eval(make_poly(poly, pos)))
    print(max_value)
