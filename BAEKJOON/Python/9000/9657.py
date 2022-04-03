"""
Title : 돌 게임 3
Link : https://www.acmicpc.net/problem/9657
"""

n = int(input())

if n in (1, 3, 4):
    print('SK')
elif n == 2:
    print('CY')
else:
    # SK / CY가 기본값, 반대인 경우만 반전
    dp = [['SK', 'CY'] for _ in range(n + 1)]
    dp[2] = ['CY', 'SK']
    for i in range(5, n + 1):
        # SK 차례일 때 기준으로 확인
        # 1, 3, 4개 적고 CY차례일 때, CY가 모두이기면 바꾸기
        if dp[i - 1][1] == 'CY' and dp[i - 3][1] == 'CY' and dp[i - 4][1] == 'CY':
            dp[i] = ['CY', 'SK']
    print(dp[n][0])
