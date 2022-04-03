"""
Title : 돌 게임
Link : https://www.acmicpc.net/problem/9655
"""

import pprint

n = int(input())

# 각 남은돌이 1 ~ n개일 때, 상근, 창영의 차례가 되면 누가 이기는지
# 4이하일 때 따로 처리하지 않기 위해 5와 n + 1중 max로 설정
dp = [['', ''] for _ in range(max(n + 1, 5))]

dp[1] = ['SK', 'CY']
dp[2] = ['CY', 'SK']
dp[3] = ['SK', 'CY']
dp[4] = ['CY', 'SK']

for i in range(5, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

pprint.pprint(dp)
# print(dp[n][0])
