"""
Title : 괄호 추가하기3
Link : https://www.acmicpc.net/problem/16639
"""

from sys import stdin

input = stdin.readline


def init_dp(dp: list, N: int, poly: str) -> list:
    for i in range(0, N, 2):
        x = int(poly[i])
        dp[i // 2][i // 2] = [x, x]
    return dp


def search_dp(dp: list, N: int, poly: str) -> int:
    for i in range(N // 2, 0, -1):
        for left in range(i):
            right = N // 2 - i + 1 + left
            values = []
            for mid in range(left, right):
                cmd = poly[mid * 2 + 1]
                values += [
                    calc(dp[left][mid][0], cmd, dp[mid + 1][right][0]),
                    calc(dp[left][mid][0], cmd, dp[mid + 1][right][1]),
                    calc(dp[left][mid][1], cmd, dp[mid + 1][right][0]),
                    calc(dp[left][mid][1], cmd, dp[mid + 1][right][1]),
                ]
            dp[left][right] = [min(values), max(values)]
    return dp[0][-1][1]


def calc(x, cmd, y):
    if cmd == "*":
        return x * y
    elif cmd == "+":
        return x + y
    return x - y


if __name__ == "__main__":
    N = int(input())
    poly = input().strip()
    dp = [[[0] * 2 for _ in range(N // 2 + 1)] for _ in range(N // 2 + 1)]
    print(search_dp(init_dp(dp, N, poly), N, poly))
