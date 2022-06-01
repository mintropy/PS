"""
Title : 국회
Link : https://www.acmicpc.net/problem/1226
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seats = []
    all_seats = 0
    for i in range(1, N + 1):
        seats.append((int(input()), i))
        all_seats += seats[-1][0]
    seats.sort(reverse=True)

    dp = [0] * 100_001

    dp = [set() for _ in range(all_seats + 1)]
    for idx, seat in enumerate(seats):
        dp[seat] = {idx + 1}
    for i in range(2, all_seats + 1):
        pass
