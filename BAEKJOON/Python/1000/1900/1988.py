"""
Title : 낮잠 시간
Link : https://www.acmicpc.net/problem/1988
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, B = map(int, input().split())
    seq = [int(input()) for _ in range(N)]
    dp = [[[0] * 2 for _ in range(N)] for _ in range(B)]
    for i in range(1, B):
        for j in range(i, N):
            x = seq[j]
            for k in range(1, i + 1):
                dp[i][j] = max(dp[i][j], dp[i - k][j - k] + x)
            # dp[i][j] = max(dp[i][j], dp[i][j - 1])
    print(max(dp[-1]))
