"""
Title : 마법사 상어와 토네이도
Link : https://www.acmicpc.net/problem/20057
"""

import sys
input = sys.stdin.readline


def move_dust(field: list, x: int, y: int, d: int):
    global dx, dy, dust_move
    # x, y 위치로 d방향으로 이동했을 때, 먼지 이동
    dust_now = field[x][y]
    field[x][y] = 0
    # 각 이동방향으로 먼지 이동
    # 범위를 벗어나면 벗어나는 먼지로 기록
    
    pass


n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

# 지금 보는 방향
direction = 3
# 지금 보는 방향으로 몇 칸을 이동하는지
moves = [i // 2 for i in range(2, n * 2 + 1)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
x = y = n // 2

# 각 방향별 먼지 이동 방향
dust_move = [
    [
        (-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1)
    ], [], [], []
]
# 다른 방향 설정
for d1, d2, v in dust_move[0]:
    dust_move[1].append((d2, -d1, v))
for d1, d2, v in dust_move[0]:
    dust_move[2].append((-d1, d2, v))
for d1, d2, v in dust_move[0]:
    dust_move[3].append((d2, d1, v))


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
