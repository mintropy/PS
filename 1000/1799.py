"""
Title : 비숍
Link : https://www.acmicpc.net/problem/1799
"""

import sys
input = sys.stdin.readline


def check(chess: list, i: int, j: int) -> bool:
    direction = {1: (-1, 1), 2: (1, 1), 3: (1, -1), 4: (-1, -1)}
    # 어짜피 비숍을 위에서부터 확인, 놓고 있으니 위에로만 확인해도 괜찮지 않을까?
    # for d in range(1, 4 + 1):
    for d in [1, 4]:
        for k in range(1, n):
            x, y = i + direction[d][0] * k, j + direction[d][1] * k
            if x < 0 or x >= n:
                break
            if y < 0 or y >= n:
                break
            if chess[x][y] == 2:
                return False
    return True


def dfs(chess: list, bishop_idx: list, bishop_count: int):
    global bishop_able, max_bishop, ables
    if bishop_idx == ables:
        if bishop_count > max_bishop:
            max_bishop = bishop_count
        return
    # 해당 인덱스의 비숍을 사용하는 것, 사용하지 않는 것으로 dfs 실시
    dfs(chess, bishop_idx + 1, bishop_count)
    i, j = bishop_able[bishop_idx]
    if check(chess, i, j):
        chess[i][j] = 2
        dfs(chess, bishop_idx + 1, bishop_count + 1)
        chess[i][j] = 1


n = int(input())
chess = list(list(map(int, input().split())) for _ in range(n))

bishop_able = []
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            bishop_able.append((i, j))
ables = len(bishop_able)

max_bishop = 0


dfs(chess, 0, 0)
print(max_bishop)




'''
# 재미있는 아이디어이긴 한데, 비효율적 + 틀림
# 최대 개수
max_bishop = 0

# 체스판을 대각선으로 두어 탐색
# 재밌는 아이디어인듯
chess_diag = [[0] * n for _ in range(2 * (n - 1) + 1)]
# 비숍을 둘 수 있는 칸
bishop_able = []

# 원래 체스판을 대각선으로 탐색
# 오른쪽 위에서 왼쪽 아래로 내려가는 대각선
for i in range(n - 1):
    diag_idx = n // 2 - i // 2
    for j in range(i + 1):
        chess_diag[i][diag_idx + j] = chess[j][i - j]
        if chess_diag[i][diag_idx + j] == 1:
            bishop_able.append((i, diag_idx + j))
# 중간 가장 긴 대각선
for i in range(n):
    chess_diag[n - 1][i] = chess[n - 1 - i][i]
    if chess_diag[n - 1][i] == 1:
        bishop_able.append((n - 1, i))
# 중간 대각선 넘어서
for i in range(n - 1):
    diag_idx = n // 2 - (n - 2 - i) // 2
    for j in range(n - 1 - i):
        chess_diag[n + i][diag_idx + j] = chess[1 + i + j][n - 1 - j]
        if chess_diag[n + i][diag_idx + j] == 1:
            bishop_able.append((n + i, diag_idx + j))

# 탐색방법
# 세로로는 같은 대각선이므로 바로 탐색
# 가로로는 2칸씩 넘어가며 탐색
# 비숍이 놓이는 칸은 2로 두어 탐색
def dfs(chess_diag, bishop_count, bishop_idx):
    global n, bishop_able, max_bishop
    if bishop_idx == len(bishop_able):
        if bishop_count > max_bishop:
            max_bishop = bishop_count
        return
    # 해당 인덱스에 해당하는 비숍을 놓을 수 있는지
    i, j = bishop_able[bishop_idx]
    bishop_check = True
    for k in range(n):
        if k == i:
            continue
        if chess_diag[k][j] == 2:
            bishop_check = False
    for k in range(j - 2, -1, 2):
        if chess_diag[k][j] == 2:
            bishop_check = False
    for k in range(j + 2, 2 * (n - 1) + 1, 2):
        if chess_diag[k][j] == 2:
            bishop_check = False
    # dfs를 해당 비숍을 놓는 것과, 놓지 않는 것으로 실시
    if bishop_check:
        chess_diag[i][j] = 2
        dfs(chess_diag, bishop_count + 1, bishop_idx + 1)
        chess_diag[i][j] = 1
    # 해당 비숍을 사용하지 않는 경우
    dfs(chess_diag, bishop_count, bishop_idx + 1)

dfs(chess_diag, 0, 0)
print(max_bishop)
'''


'''
# 모든 점 탐색 : 시간초과
def check(chess, i, j):
    global n
    dx, dy = [-1, -1, 1, 1], [-1, 1, 1, -1]
    for d in range(4):
        for m in range(n):
            x, y = i + dx[d] * m, j + dy[d] * m
            if x < 0 or x >= n:
                break
            if y < 0 or y >= n:
                break
            if chess[x][y] == 2:
                return False
    return True


def dfs(chess, i, j, bishop_count):
    global n, max_bishop
    # 모든 범위를 다 탐색하였을 때 결과 확인
    if i == n - 1 and j == n:
        if bishop_count > max_bishop:
            max_bishop = bishop_count
        return
    # 줄을 넘어가면 i, j 조정하여 탐색
    while True:
        if i == n - 1 and j == n:
            dfs(chess, i, j, bishop_count)
            return
        elif i <= n - 1 and j == n:
            i += 1
            j = 0
        if chess[i][j] == 1:
            # 비숍을 놓을 수 있는지 확인
            if check(chess, i, j):
                chess[i][j] = 2
                dfs(chess, i, j + 1, bishop_count + 1)
                chess[i][j] = 1
        j += 1


n = int(input())
# 비숍을 놓을 수 있는 칸 1, 비숍이 있는 칸 2로 표시
chess = [list(map(int, input().split())) for _ in range(n)]
max_bishop = 0

dfs(chess, 0, 0, 0)
print(max_bishop)
'''