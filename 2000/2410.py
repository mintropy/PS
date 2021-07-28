"""
Title : 2의 멱수의 합
Link : https://www.acmicpc.net/problem/2410
"""

import sys
input = sys.stdin.readline

n = int(input())
power_of_2 = [2 ** i for i in range(0, 30)]

dp = [0 for _ in range(n // 2 + 1)]
dp[0] = 1



'''
# 2차원 DP 메모리 초과
dp = [[0] * 30 for _ in range(n // 2 + 1)]
dp[0][0] = 1

for m in range(1, n // 2 + 1):
    for j in range(30):
        p = power_of_2[j]
        if p > 2 * m:
            break
        elif p == 2 * m:
            dp[m][j] = 1
            break
        else:
            # m - p 에서 탐색
            # 최대 p를 사용한 조합까지만 탐색
            dp[m][j] = sum(dp[(2 * m - p) // 2][:j + 1]) % 1_000_000_000

print(sum(dp[-1]))
'''


'''
# 메모리 초과 / 절반으로 줄여보자
dp = [[0] * 30 for _ in range(n + 1)]

for m in range(1, n + 1):
    for j in range(30):
        p = power_of_2[j]
        if p > m:
            break
        elif p == m:
            dp[m][j] = 1
            break
        else:
            # m - p 에서 탐색
            # 최대 p를 사용한 조합까지만 탐색
            dp[m][j] = sum(dp[m - p][:j + 1])

print(sum(dp[-1]))
'''