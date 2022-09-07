"""
Title : 숫자 게임
Link : https://www.acmicpc.net/problem/2303
"""

from itertools import combinations
from sys import stdin

input = stdin.readline


def solution(cards: list[tuple[int]]) -> int:
    ans = max_unit_digit = 0
    for idx, card in enumerate(cards):
        _max_unit_digit = 0
        for comb in combinations(card, 3):
            unit_digit = sum(comb) % 10
            if _max_unit_digit < unit_digit:
                _max_unit_digit = unit_digit
        if max_unit_digit <= _max_unit_digit:
            ans = idx + 1
            max_unit_digit = _max_unit_digit
    return ans


if __name__ == "__main__":
    N = int(input())
    cards = [tuple(map(int, input().split())) for _ in range(N)]
    print(solution(cards))
