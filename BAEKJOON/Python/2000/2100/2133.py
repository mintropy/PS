"""
Title : 타일 채우기
Link : https://www.acmicpc.net/problem/2133
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    if N % 2:
        print(0)
    else:
        dp = [0] * (N // 2 + 1)
        dp[0] = 1
        dp[1] = 3
        for i in range(2, N // 2 + 1):
            tmp = 0
            for j in range(i):
                tmp += dp[j] * dp[i - 1 - j] * 3
            dp[i] = tmp
        print(dp[-1])
