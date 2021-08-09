"""
Title : 확장 게임
Link : https://www.acmicpc.net/problem/16920
"""

import sys, collections
input = sys.stdin.readline


def dfs(player: str, x: int, y: int, s_i: int):
    global n, m, s, game_board
    global dx, dy
    global next_castle, next_castle_check_count
    if s_i == 0:
        return
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if game_board[nx][ny] == '.':
                game_board[nx][ny] = player
                next_castle.append((nx, ny))
                next_castle_check_count += 1
                dfs(player, nx, ny, s_i - 1)


n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))

game_board = [list(input()) for _ in range(n)]
# 각 플레이어의 성의 개수
castle = [0] * (p + 1)

# 각 플레이어의 가장 최근 성 위치 & 확인해야할 성 개수
castle_check = [[] * (p + 1)]
castle_check_count = 0
for i in range(n):
    for j in range(m):
        try:
            k = int(game_board[i][j])
            castle[k] += 1
            castle_check[k].append((i, j))
            castle_check_count += 1
        except:
            continue


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

while True:
    if not castle_check_count:
        break
    next_castle_check = [[] * (p + 1)]
    next_castle_check_count = 0
    # 1번 플레이어부터 p번 플레이어까지 순회
    for i in range(1, p + 1):
        # 각 플레이어가 이동 가능한 만큼 탐색
        # 새로 탐색한 성 구역
        next_castle = []
        for c in castle_check[i]:
            dfs(str(i), *c, s[i])
        next_castle_check[i] = next_castle
        castle[i] += len(next_castle)
    if not next_castle_check_count:
        break
    castle_check = next_castle_check
    castle_check_count = next_castle_check_count

print(*castle[1:])