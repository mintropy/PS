"""
Title : 비숍
Link : https://www.acmicpc.net/problem/1799
"""

'''
https://suri78.tistory.com/184
https://yanoo.tistory.com/47
'''

import sys
input = sys.stdin.readline


def dfs(bishop_count: int, bishop_idx: int, bishop_able: list, ables: int):
    global n, max_bishop, check_diag_1, check_diag_2
    if bishop_idx == ables:
        if bishop_count > max_bishop:
            max_bishop = bishop_count
        return
    # 비숍을 추가하지 않고 탐색
    dfs(bishop_count, bishop_idx + 1, bishop_able, ables)
    # 해당 비숍을 놓을 수 있는지 확인 > 추가하고 탐색
    # 몇번째 대각선인지 찾기
    # diag_1은 두 좌표의 합으로 해당 대각선 지정
    # diag_2는 n - 1 - j + i로 지정
    i, j = bishop_able[bishop_idx]
    diag_1_idx = i + j
    diag_2_idx = n - 1 - j + i
    # 두 대각선 모두 놓을 수 있으면 진행
    if not check_diag_1[diag_1_idx] and not check_diag_2[diag_2_idx]:
        check_diag_1[diag_1_idx] = True
        check_diag_2[diag_2_idx] = True
        dfs(bishop_count + 1, bishop_idx + 1, bishop_able, ables)
        check_diag_1[diag_1_idx] = False
        check_diag_2[diag_2_idx] = False


n = int(input())
chess = list(list(map(int, input().split())) for _ in range(n))

# 각 대각선이 가능한지만 확인하면 됨
# 각 대각선에 놓게되면 True로 변경
# 1은 오른쪽 위에서 왼쪽 아래로
# 2는 왼쪽 위에서 오른쪽 아래로 가는 대각선
# 대각선의 개수 : (n - 1) * 2 + 1
check_diag_1 = [False] * ((n - 1) * 2 + 1)
check_diag_2 = [False] * ((n - 1) * 2 + 1)

bishop_able_black = []
bishop_able_white = []
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            if (i + j) % 2 == 0:
                bishop_able_black.append((i, j))
            else:
                bishop_able_white.append((i, j))
                
#  가능한 자리의 수 == 비숍을 놓을 수 있는 자리의 개수
blakc_ables = len(bishop_able_black)
white_ables = len(bishop_able_white)

answer = 0

max_bishop = 0
dfs(0, 0, bishop_able_black, blakc_ables)
answer += max_bishop
max_bishop = 0
dfs(0, 0, bishop_able_white, white_ables)
answer += max_bishop
print(answer)


'''
def check(bishop_idx: list) -> bool:
    global bishop_able, bishop_used
    # 어짜피 대각선에 있으니깐, 한칸씩 이동하며 탐색하는 대신
    # 좌표사이 차이로만 비교해도 괜찮다 !!
    # & 비숍을 위에서부터 확인했으니, 해당 인댁스 이전까지만 확인
    i, j = bishop_able[bishop_idx]
    for k in range(bishop_idx):
        if bishop_used[k]:
            x, y = bishop_able[k]
            if abs(i - x) == abs(j - y):
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
    if check(bishop_idx):
        bishop_used[bishop_idx] = True
        dfs(chess, bishop_idx + 1, bishop_count + 1)
        bishop_used[bishop_idx] = False


# 체스판에 모두 기록할 필요가 없다
n = int(input())
chess = list(list(map(int, input().split())) for _ in range(n))

bishop_able = []
for i in range(n):
    for j in range(n):
        if chess[i][j] == 1:
            bishop_able.append((i, j))
#  가능한 자리의 수 == 비숍을 놓을 수 있는 자리의 개수
ables = len(bishop_able)
bishop_used = [False] * ables

max_bishop = 0


dfs(chess, 0, 0)
print(max_bishop)
'''


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