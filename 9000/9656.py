"""
Title : 돌 게임 2
Link : https://www.acmicpc.net/problem/9656
"""

n = int(input())

if n % 2:
    print('CY')
else:
    print('SK')
"""
if n == 1:
    print('CY')
elif n == 2:
    print('SK')
else:
    # 기본값은 상근이, 창영이가 이길때만 변경
    dp = [['SK', 'SK'] for _ in range(n + 1)]
    dp[1][0] = 'CY'
    dp[2][1] = 'CY'
    for i in range(3, n + 1):
        
"""
