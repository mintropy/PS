"""
Title : 리조트
Link : https://www.acmicpc.net/problem/13302
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

price = [10000, 25000, 37000]

# 1일권만, 연속 3일 3일권, 연속 2일 3일권
# 연속 5일 5일권, 4일 5일권
dp = [[[0, 0] for _ in range(n + 1)] for _ in range(5)]

for d in arr:
    for i in range(3):
        dp[i][d][0] = -1

for d in range(1, n + 1):
    # 가능한 날
    if not dp[0][d][0]:
        dp[0][d][0] = 10000 + dp[0][d - 1][0]
    # 불가능한 날
    else:
        dp[0][d][0] = dp[0][d - 1][0]


# 3일권
# 연속 3일중 며칠이 가능한지
day_count = 0

