"""
Title : 마법사 상어와 토네이도
Link : https://www.acmicpc.net/problem/20057
"""

import sys
input = sys.stdin.readline






n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

# 지금 보는 방향
direction = 3
# 지금 보는 방향으로 몇 칸을 이동하는지
moves = [i // 2 for i in range(2, n * 2 + 1)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
x = y = n // 2

# 경계 밖으로 벗어난 먼지
dust_outside = 0
for dist in moves:
    # 지금 보는 방향으로 앞으로 진행
    for _ in range(dist):
        # 한 칸 앞으로 진행
        x, y = x + dx[direction], y + dy[direction]
        # 먼지 밀어내기
        
        pass
    # 진행 방향을 반시계 90도 회전
    d = (d - 1) % 4

print(dust_outside)
