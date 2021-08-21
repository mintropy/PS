"""
Title : 스도쿠
Link : https://www.acmicpc.net/problem/2239
"""

import sys
# import pprint
input = sys.stdin.readline


def dfs(i: int, j: int):
    global sudoku, sudoku_col, sudoku_row, sudoku_sq
    if i == 9:
        # 스도쿠 완성
        for line in sudoku:
            print(*line, sep = '')
        # 종료
        exit()
    # j값에 따라 조정
    if j == 9:
        i += 1
        j = 0
        dfs(i, j)
    # 아니라면 탐색
    # 연속해서 숫자가 채워진 칸인경우, while로 원하는 위치까지 넘어가기
    while True:
        # 1. 해당칸에 숫자가 있는지 확인
        if not sudoku[i][j]:
            # 해당 칸에 1부터 9까지 확인
            # 사각형, 행, 열 모두 가능하면 재귀 넘기기
            # 아니면 넘어가기
            for num in range(1, 10):
            # for num in range(9, 0, -1):
                if not(1 << num & sudoku_row[i]) and not(1 << num & sudoku_col[j]) and not(1 << num & sudoku_sq[(i // 3) * 3 + j // 3]):
                    # 스도쿠 갱신
                    sudoku[i][j] = num
                    # row, col, sq에 추가
                    sudoku_row[i] |= 1 << num
                    sudoku_col[j] |= 1 << num
                    sudoku_sq[(i // 3) * 3 + j // 3] |= 1 << num
                    dfs(i, j + 1)
                    # 스도쿠 갱신
                    sudoku[i][j] = 0
                    # row, col, sq에서 제거
                    sudoku_row[i] &= ~(1 << num)
                    sudoku_col[j] &= ~(1 << num)
                    sudoku_sq[(i // 3) * 3 + j // 3] &= ~(1 << num)
            # 모든 숫자 확인했으면 돌아가기
            return
        # 2. 숫자가 있으면 한칸 전진
        else:
            j += 1
            # 조정
            if j == 9:
                i += 1
                j = 0
            # i == 9에 도달하면 재귀 넘기기
            if i == 9:
                dfs(i, j)
                return

sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]
'''
# 스도쿠의 행
sudoku_row = [set() for _ in range(9)]
# 스도쿠의 열
sudoku_col = [set() for _ in range(9)]
# 왼쪽위부터 오른쪽아래까지 순서대로
sudoku_sq = [set() for _ in range(9)]
# 값 입력
for i in range(9):
    sudoku_row[i].update(sudoku[i])
    sudoku_col[i].update([sudoku[k][i] for k in range(9)])
for i in range(3):
    for j in range(3):
        for k in range(3):
            sudoku_sq[i * 3 + j].update(sudoku[i * 3 + k][j * 3:(j + 1) * 3])
'''
# 비트마스킹으로
sudoku_row = [0] * 9 
sudoku_col = [0] * 9 
sudoku_sq = [0] * 9 

# 값 입력
for i in range(9):
    for j in range(9):
        sudoku_row[i] |= 1 << sudoku[i][j]
        sudoku_col[i] |= 1 << sudoku[j][i]
for i in range(3):
    for j in range(3):
        for k in range(9):
            sudoku_sq[i * 3 + j] |= 1 << sudoku[i * 3 + k // 3][j * 3 + k % 3]


dfs(0, 0)



'''
# 시간초과
# 함수 호출 많아서 그런듯
def dfs(i: int, j: int):
    global sudoku, ans_sudoku
    if i == 9:
        # 스도쿠 완성
        for line in sudoku:
            print(*line, sep = '')
        sys.exit()
    # j값에 따라 조정
    if j == 9:
        i += 1
        j = 0
        dfs(i, j)
    # 아니라면 탐색
    # 연속해서 숫자가 채워진 칸인경우, while로 원하는 위치까지 넘어가기
    while True:
        # 1. 해당칸에 숫자가 있는지 확인
        if not sudoku[i][j]:
            # 해당 칸에 1부터 9까지 확인
            # 사각형, 행, 열 모두 가능하면 재귀 넘기기
            # 아니면 넘어가기
            for num in range(1, 10):
                if check_sq(i, j, num) and check_row(i, j, num) and check_col(i, j, num):
                    sudoku[i][j] = num
                    dfs(i, j + 1)
                    sudoku[i][j] = 0
            # 모든 숫자 확인했으면 돌아가기
            return
        # 2. 숫자가 있으면 한칸 전진
        else:
            j += 1
            # 조정
            if j == 9:
                i += 1
                j = 0
            # i == 9에 도달하면 재귀 넘기기
            if i == 9:
                dfs(i, j)
                return


def check_sq(i:int, j:int, num: int):
    """
    해당 위치가 속한 사각형 확인
    """
    global sudoku
    check = [False] * 10
    check[num] = True
    for k in range((i // 3) * 3, (i // 3 + 1) * 3):
        for l in range((j // 3) * 3, (j // 3 + 1) * 3):
            # 해당 위치가 0이면 넘거가기
            if not sudoku[k][l]:
                continue
            # 0이 아닌 숫자가 있을때는 확인
            elif not check[sudoku[k][l]]:
                check[sudoku[k][l]] = True
            else:
                return False
    return True


def check_row(i:int, j:int, num: int):
    """
    해당 위치가 속한 열 확인
    """
    global sudoku
    check = [False] * 10
    check[num] = True
    # 해당 열을 모두 돌면서 확인
    for k in range(9):
        # 해당 위치가 0이면 넘거가기
        if not sudoku[i][k]:
            continue
        # 0이 아닌 숫자가 있을때는 확인
        elif not check[sudoku[i][k]]:
            check[sudoku[i][k]] = True
        else:
            return False
    return True


def check_col(i:int, j:int, num: int):
    """
    해당 위치가 속한 행 확인
    """
    global sudoku
    check = [False] * 10
    check[num] = True
    # 해당 열을 모두 돌면서 확인
    for k in range(9):
        # 해당 위치가 0이면 넘거가기
        if not sudoku[k][j]:
            continue
        # 0이 아닌 숫자가 있을때는 확인
        elif not check[sudoku[k][j]]:
            check[sudoku[k][j]] = True
        else:
            return False
    return True


sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]

dfs(0, 0)
'''