"""
Title : 동전 2
Link : https://www.acmicpc.net/problem/2294
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    for _ in range(n):
        coin = int(input())
        for i in range(k, 0, -1):
            if dp[i] and i + coin <= n + 1:
                dp[i + coin] = dp[i] + 1
        dp[coin] = 1
    print(dp[k])
