"""
Title : 가장 긴 감소하는 부분 수열
Link : https://www.acmicpc.net/problem/11722
"""


import sys

n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if seq[i] < seq[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))