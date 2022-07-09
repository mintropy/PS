"""
Title : 너의 티어는?
Link : https://www.acmicpc.net/problem/14613
"""

import sys, math
input = sys.stdin.readline

w, l, d = map(float, input().split())

# 지금 2000점
# 브론즈 1500 미만
# 실버 2000 미만
# 골드 2500 미만 
# 플래티넘 3000 미만
# 다이아 3500 미만 >> 20연승

rank = [0] * 5
# 무승부 확률이 0일때와 아닐때로 구분
if d == 0:
    # 이기는 판을 0 ~ 20경기로 나누어 계산
    for win in range(21):
        rate = math.factorial(20) // (math.factorial(win) * math.factorial(20 - win))
        rating = 2000 + 50 * win - 50 * (20 - win)
        if rating < 1500:
            rank[0] += rate
        elif rating < 2000:
            rank[1] += rate
        elif rating < 2500:
            rank[2] += rate
        elif rating < 3000:
            rank[3] += rate
        else:
            rank[4] += rate
    
    base = 2 ** 20
    for c in rank:
        print(f'{(c/base):.8f}')
else:
    # draw가 몇 번 나올 확률
    base = [2 ** i for i in range(21)]
    for draw in range(21):
        # 무승부가 draw개인 개수
        base_draw = math.factorial(20) // (math.factorial(draw) * math.factorial(20 - draw))
        for win in range(21 - draw):
            # 이기는 경우의 수
            rate = math.factorial(20 - draw) // (math.factorial(win) * math.factorial(20 - draw - win))
            rate /= base[draw]
            rate = base_draw * rate
            rating = 2000 + 50 * win - 50 * (20 - draw - win)
            if rating < 1500:
                rank[0] += rate
            elif rating < 2000:
                rank[1] += rate
            elif rating < 2500:
                rank[2] += rate
            elif rating < 3000:
                rank[3] += rate
            else:
                rank[4] += rate
    
    for c in rank:
        print(f'{c / (10 ** 8):.8f}')
