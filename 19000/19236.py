"""
Title : 청소년 상어
Link : https://www.acmicpc.net/problem/19236
"""

import sys
input = sys.stdin.readline


def dfs(i: int, j: int, fish_eaten: int):
    global fish, fish_by_num, max_fish
    # 상어 위치 i, j
    # 물고기 이동
    pass


def fish_move():
    global fish, fish_by_num, direction
    for i in range(1, 17):
        # 물고기가 살아 있을 때
        if fish_by_num:
            x, y = fish_by_num[i]
            d = fish[i][j + 2 + 1]
            while True:
                # 해당 방향으로 움직일 수 있는지 확인
                nx, ny = x + direction[d][0], y + direction[d][1]
                if fish[nx][ny * 2] <= 16:
                    pass
                else:
                    pass





fish = [list(map(int, input().split())) for _ in range(4)]
# 물고기 번호별 위치 저장
fish_by_num = [[] for _ in range(17)]
for i in range(4):
    for j in range(4):
        fish_by_num[fish[i][j * 2]] = [i, j]
# 이동하는 8방향
direction = {
    1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1),
    5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)
}

# 상어는 20, 빈칸은 0으로 판별
fish[0][0] = 20

max_fish = 1
