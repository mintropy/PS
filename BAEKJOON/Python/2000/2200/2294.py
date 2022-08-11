"""
Title : 동전 2
Link : https://www.acmicpc.net/problem/2294
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [100_000] * (k + 1)
    dp[0] = 0
    for _ in range(n):
        coin = int(input())
        for i in range(coin, k + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
    if dp[k] == 100_000:
        print(-1)
    else:
        print(dp[k])
