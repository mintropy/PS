"""
Title : 계단 수
Link : https://www.acmicpc.net/problem/1562
"""

from sys import stdin

input = stdin.readline


def solve(n: int, x: int, a: int):
    if n < 10:
        return 0
    elif n == 10:
        return 1
    c = dp[n][x][a]
    if c != -1:
        return c
    c = 0
    if x >= 1:
        c += solve(n - 1, x - 1, (a | 1 << (x - 1)) % mod)
    if x <= 8:
        c += solve(n - 1, x + 1, (a | 1 << (x + 1)) % mod)


def search():
    pass


if __name__ == "__main__":
    n = int(input())
    mod = 1_000_000_000
    dp = [[[-1] * 1024 for _ in range(10)] for _ in range(n + 1)]
    print(solve(n))
