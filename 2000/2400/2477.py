"""
Title : 참외밭
Link : https://www.acmicpc.net/problem/2477
"""

import sys
input = sys.stdin.readline


k = int(input())
cor = []
cmd = []
x = y = 0
for _ in range(6):
    d, l = map(int, input().split())
    if d == 1:
        y += l
    elif d == 2:
        y -= l
    elif d == 3:
        x += l
    else:
        x -= l
    cor.append((x, y))
    cmd.append((d, l))


ans = 0
# 큰 사각형 찾기
cor_x = sorted(cor)
min_x = cor_x[0][0]
max_x = cor_x[-1][0]

cor_y = sorted(cor, key= lambda x:x[1])
min_y = cor_y[0][1]
max_y = cor_y[-1][1]

ans += (max_x - min_x) * (max_y - min_y)

# 빠지는 부분 찾기
for i in range(6):
    x, y = cor[i]
    if min_x < x < max_x and min_y < y < max_y:
        mid_x = x
        mid_y = y
        idx = i
        break

mid_x1, mid_y1 = cor[i - 1]
mid_x2, mid_y2 = cor[(i + 1) % 6]

ans -= abs(mid_x1 - mid_x2) * abs(mid_y1 - mid_y2)

# 출력
print(ans * k)
