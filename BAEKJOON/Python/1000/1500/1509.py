"""
Title : 팰린드롬 분할
Link : https://www.acmicpc.net/problem/1509
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    s = " " + input().strip()
    l = len(s)
    dp = [i for i in range(l)]
    for i in range(2, l):
        dp[i] = dp[i - 1] + 1
        for j in range(i - 1, 0, -1):
            tmp = s[j : i + 1]
            if tmp == tmp[::-1]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    print(dp[-1])
