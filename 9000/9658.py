"""
Title : 돌 게임 4
Link : https://www.acmicpc.net/problem/9658
"""

n = int(input())

if n == 1 or n == 3:
    print('CY')
elif n == 2 or n == 4:
    print('SK')
else:
    dp = [['SK'] * 2 for _ in range(n + 1)]
    dp[1][0] = dp[3][0] = 'CY'
    dp[2][1] = dp[4][1] = 'CY'
    for i in range(5, n + 1):
        # 상근이 쪽은 모두 다 창영이면 바꾸기
        if dp[i - 1][1] == 'CY' and dp[i - 3][1] == 'CY' and dp[i - 4][1] == 'CY':
            dp[i][0] = 'CY'
        # 창영이 쪽은 한 번이라도 창영이가 있으면 바꾸기
        if dp[i - 1][0] == 'CY' or dp[i - 3][0] == 'CY' or dp[i - 4][0] == 'CY':
            dp[i][1] = 'CY'
    print(dp[n][0])
