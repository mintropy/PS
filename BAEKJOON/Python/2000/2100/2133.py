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
    dp[0] = 1
    for i in range(1, N // 2 + 1):
        tmp = dp[i - 1] * 3
        for j in range(0, i - 1):
            tmp += dp[j] * 2
        dp[i] = tmp
    return dp[-1]


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
