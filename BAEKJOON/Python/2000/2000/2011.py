"""
Title : 암호코드
Link : https://www.acmicpc.net/problem/2011
"""

from sys import stdin

input = stdin.readline


def solve(N: list[int]) -> int:
    if len(N) == 1:
        if N[0]:
            return 1
        return 0
    l = len(N)
    dp = [[0, 0] for _ in range(l)]
    if N[0]:
        dp[0][0] = 1
    if l > 1:
        if N[1]:
            dp[1][0] = dp[0][0]
        if 10 <= get_next_num(N, 1) <= 26:
            dp[1][1] = 1
    mod = 1_000_000
    for i in range(2, l):
        if N[i]:
            dp[i][0] = sum(dp[i - 1]) % mod
        if 10 <= get_next_num(N, i) <= 26:
            dp[i][1] = sum(dp[i - 2]) % mod
    return sum(dp[-1]) % mod


def get_next_num(N: list[int], idx: int) -> int:
    return N[idx - 1] * 10 + N[idx]


if __name__ == "__main__":
    N = [int(x) for x in input().strip()]
    print(solve(N))
