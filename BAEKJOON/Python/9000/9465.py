"""
Title : 스티커
Link : https://www.acmicpc.net/problem/9465
"""

import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = []
    for i in range(2):
        dp.append(stickers[i][::])
    
    # 스티커 두번째 줄
    if n >= 2:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    # 스티커 길이가 3이상일 때
    if n >= 3:
        for i in range(2, n):
            sticker_up = [dp[0][i - 2], dp[1][i - 2], dp[1][i - 1]]
            sticker_down = [dp[0][i - 2], dp[0][i - 1], dp[1][i - 2]]
            dp[0][i] += max(sticker_up)
            dp[1][i] += max(sticker_down)
    
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        print(max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2]))
