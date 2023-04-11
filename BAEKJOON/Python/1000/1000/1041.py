"""
Title : 주사위
Link : https://www.acmicpc.net/problem/1041
"""

from sys import stdin

input = stdin.readline


class Dice:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers: list[int] = numbers
        A, B, C, D, E, F = self.numbers
        self.min1 = min(self.numbers)
        self.min2 = min(
            A + B,
            B + F,
            F + E,
            E + A,
            A + D,
            D + F,
            F + C,
            C + A,
            B + D,
            D + E,
            E + C,
            C + B,
        )
        self.min3 = min(
            A + C + E,
            A + E + D,
            A + D + B,
            A + B + C,
            F + C + E,
            F + E + D,
            F + D + B,
            F + B + C,
        )


if __name__ == "__main__":
    N: int = int(input())
    numbers: list[int] = list(map(int, input().split()))
    if N == 1:
        print(sum(numbers) - max(numbers))
    else:
        dice = Dice(numbers)
        ans: int = (
            dice.min1 * (((N - 2) ** 2) * 5 + (N - 2) * 4)
            + dice.min2 * ((N - 1) * 4 + (N - 2) * 4)
            + dice.min3 * 4
        )
        print(ans)
