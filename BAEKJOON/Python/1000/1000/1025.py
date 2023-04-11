"""
Title : 제곱수 찾기
Link : https://www.acmicpc.net/problem/1025
"""

from sys import stdin

input = stdin.readline


def square_validation(positions: list[tuple[int]]) -> bool:
    pass


if __name__ == "__main__":
    N, M = map(int, input().split())
    number_map: list[list[int]] = [
        list(int(x) for x in input().strip()) for _ in range(N)
    ]
    numbers: dict[int, list[tuple[int]]] = {x: [] for x in range(1, 10)}
    for i, line in enumerate(number_map):
        for j, x in enumerate(line):
            numbers[x].append(i, j)

    max_square: int = 9 if numbers[9] else 4 if numbers[4] else 1 if numbers[1] else -1
    for x in range(4, int(max(N, M) ** 0.5) + 1):
        square = x * x
        positions = []
        while square:
            positions.append(square % 10)
            square //= 10
