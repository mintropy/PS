"""
Title : 가장 긴 증가하는 부분 수열 4
Link : https://www.acmicpc.net/problem/14002
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    A = int(input())
    seq = list(map(int, input().split()))

    dp = [1] * A
    for i in range(A):
        for j in range(i + 1):
            if dp[i] < dp[j] + 1 and seq[i] > seq[j]:
                dp[i] = dp[j] + 1

    LIS_length = max(dp)
    ans = [0] * LIS_length
    idx = LIS_length - 1
    for i in range(A - 1, -1, -1):
        if dp[i] == idx + 1:
            ans[idx] = seq[i]
            idx -= 1
            if idx == -1:
                break
    print(LIS_length)
    print(*ans)
