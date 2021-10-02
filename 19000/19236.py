"""
Title : 청소년 상어
Link : https://www.acmicpc.net/problem/19236
"""

import copy
import sys
input = sys.stdin.readline


def dfs(i: int, j: int, fish: list):
    global fish_by_num, max_fish, direction
    # 상어 위치 i, j
    # 더 먹는 물고기
    additional_fish = 0
    # 상어 방향
    dx, dy = direction[fish[i][j * 2 + 1]]
    for k in range(1, 5):
        # 범위를 벗어나면 종료
        ni, nj = i + dx * k, j + dy * k
        if ni < 0 or ni >= 4 or nj < 0 or nj >=4 :
            break
        # 해당 위치에 물고기가 있을 때
        if fish[ni][nj * 2] > 0:
            # 상어가 이동할 위치 물고기 번호
            fish_num = fish[ni][nj * 2]
            fish_pos = [ni, nj]
            # 상어를 해당 위치로 이동
            fish[i][j * 2] = 0
            fish[ni][nj * 2] = 20
            fish_by_num[fish_num] = []
            # 추가 탐색
            more_additional_fish = dfs(ni, nj, fish_move(copy.deepcopy(fish)))
            # 상어 이동 복귀
            fish[i][j * 2] = 20
            fish[ni][nj * 2] = fish_num
            fish_by_num[fish_num] = fish_pos
            # 최댓값 비교
            if additional_fish < more_additional_fish + fish_num:
                additional_fish = more_additional_fish + fish_num
    return additional_fish


def fish_move(fish: list) -> list:
    # 물고기 이동
    global fish_by_num, direction
    for i in range(1, 17):
        # 물고기가 살아 있을 때
        if fish_by_num[i]:
            # 해당 물고기 위치, 방향
            x, y = fish_by_num[i]
            d = fish[x][y * 2 + 1]
            while True:
                # 해당 방향으로 움직일 수 있는지 확인
                nx, ny = x + direction[d][0], y + direction[d][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    fish_num = fish[nx][ny * 2]
                    # 해당 위치에 다른 물고기가 있거나, 비어 있다면
                    if fish_num <= 16:
                        # 빈 자리면 그대로 이동
                        if fish_num == 0:
                            fish[nx][ny * 2], fish[nx][ny * 2 + 1] = fish[x][y * 2], fish[x][y * 2 + 1]
                            fish[x][y * 2] = 0
                            # 물고기 정보 바꾸기
                            fish_by_num[i] = [nx, ny]
                        # 물고기가 있으면, 위치 교체
                        else:
                            fish[nx][ny * 2], fish[x][y * 2] = fish[x][y * 2], fish[nx][ny * 2]
                            fish[nx][ny * 2 + 1], fish[x][y * 2 + 1] = fish[x][y * 2 + 1], fish[nx][ny * 2 + 1]
                            # 두 물고기 정보 교환
                            fish_by_num[i] = [nx, ny]
                            fish_by_num[fish_num] = [x, y]
                        break
                d -= 1
                if d == 0:
                    d = 8
    return fish



# 물고기 번호, 방향
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
fish_eaten_num = fish[0][0]
fish[0][0] = 20
fish_by_num[fish_eaten_num] = []

shark = [0, 0]

print(dfs(*shark, fish) + fish_eaten_num)
