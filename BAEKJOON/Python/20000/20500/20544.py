"""
Title : 공룡게임
Link : https://www.acmicpc.net/problem/20544
"""

import sys
sys.setrecursionlimit(10_000)
input = sys.stdin.readline


def solve(pos, now, before, two_before):
    global N, dp, MOD
    tmp = dp[pos][now][before][two_before]
    if pos == N - 1:
        if two_before:
            return 1
        else:
            return tmp
    if tmp:
        return tmp
    if now == 0:
        tmp += solve(pos + 1, 0, now, two_before) + solve(pos + 1, 1, now, two_before) + solve(pos + 1, 2, now, True)
    elif now == 1:
        if not before:
            tmp += solve(pos + 1, 0, now, two_before) + solve(pos + 1, 1, now, two_before) + solve(pos + 1, 2, now, True)
        else:
            tmp += solve(pos + 1, 0, now, two_before)
    else:
        if not before:
            tmp += solve(pos + 1, 0, now, two_before) + solve(pos + 1, 1, now, two_before)
        else:
            tmp += solve(pos + 1, 0, now, two_before)
    return tmp % MOD


if __name__ == "__main__":
    N = int(input())
    dp = [[[[0] * 2 for _ in range(3)] for _ in range(3)] for _ in range(N + 1)]
    MOD = 1_000_000_007
    print(solve(0, 0, 0, False))
