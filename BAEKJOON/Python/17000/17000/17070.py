"""
Title : 파이프 옮기기 1
Link : https://www.acmicpc.net/problem/17070
"""

import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
# dp의 각 자리는 경의우 수 & 방향
# 0: 오른쪽, 1: 대각선, 2: 아래
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if room[i][j] == 1 or (i == 0 and j == 1):
            continue
        # 각 점마다 세 방향 탐색
        # 오른쪽으로 이동
        if j != 0:
            dp[i][j][0] = sum(dp[i][j - 1][:2])
        # 아래로 이동
        if i != 0:
            dp[i][j][2] = sum(dp[i - 1][j][1:])
        # 대각선으로 이동
        if i != 0 and j != 0:
            # 바로 위, 왼쪽 칸 확인
            if room[i][j - 1] == 1 or room[i - 1][j] == 1:
                continue
            dp[i][j][1] = sum(dp[i - 1][j - 1])

print(sum(dp[-1][-1]))