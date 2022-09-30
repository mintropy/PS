"""
Title : 타일 채우기
Link : https://www.acmicpc.net/problem/2133
"""

from sys import stdin

input = stdin.readline


def solve(N: int) -> int:
    if N % 2:
        return 0
    dp = [0] * (N // 2 + 1)
    dp[1] = 3
    for i in range(2, N // 2 + 1):
        dp[i] = dp[i - 1] * 3
        for j in range(2, i):
            dp[i] += dp[i - j] * 2
        dp[i] += 2
    return dp[-1]


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
