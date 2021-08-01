"""
Title : 200년간 폐관수련했더니 PS 최강자가 된 건에 대하여
Link : https://www.acmicpc.net/problem/19582
"""

n = int(input())

# 첫번째는 총 상금, 두번째는 최대 상금, 세번째는 한 경기라도 참석하지 못했는지
dp = [0, 0, 0]

for _ in range(n):
    x, p = map(int, input().split())
    # 모든 상금을 딸 수 있을 때
    if dp[0] + p <= x:
        dp[0] += p
        if p > dp[1]:
            dp[1] = p
    elif dp[0] + p > x:
        tmp = dp[0] - dp[1]
        # 이전 참가 못한 대회있는지에 따라 경우의 수 나뉨
        # 모든 대회를 참가했었던 경우
        if dp[2] != -1:
            if tmp <= x:
                dp[0] = tmp + p
                dp[1] = p
                dp[2] = -1
            else:
                print('Zzz')
                break
        else:
            print('Zzz')
            break
else:
    print('Kkeo-eok')