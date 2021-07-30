"""
Title : 비숍
Link : https://www.acmicpc.net/problem/1799
"""

import sys
input = sys.stdin.readline


n = int(input())
chess = list(list(map(int, input().split())) for _ in range(n))

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
def dfs(chess_diag, i, j, bishop_count, bishop_idx):
    global n, bishop_able
    pass




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