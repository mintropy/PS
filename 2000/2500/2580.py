"""
Title : 스도쿠
Link : https://www.acmicpc.net/problem/2850
"""

import sys
input = sys.stdin.readline


def solve_sudoku(n):
    global sudoku, sudoku_row, sudoku_col, sudoku_sq
    if n == 81:
        for line in sudoku:
            print(*line)
        # return True
        exit()
    x, y = n // 9, n % 9
    if sudoku[x][y]:
        # return solve_sudoku(n + 1)
        solve_sudoku(n + 1)
    else:
        for i in range(1, 10):
            if not sudoku_row[x][i] and not sudoku_col[y][i] and not sudoku_sq[(x // 3) * 3 + y // 3][i]:
                sudoku_row[x][i] = sudoku_col[y][i] = sudoku_sq[(x // 3) * 3 + y // 3][i] = True
                sudoku[x][y] = i
                # if solve_sudoku(n + 1):
                #     return True
                solve_sudoku(n + 1)
                sudoku_row[x][i] = sudoku_col[y][i] = sudoku_sq[(x // 3) * 3 + y // 3][i] = False
                sudoku[x][y] = 0
    # return False


sudoku = [list(map(int, input().split())) for _ in range(9)]
sudoku_row = [[False] * 10 for _ in range(9)]
sudoku_col = [[False] * 10 for _ in range(9)]
sudoku_sq = [[False] * 10 for _ in range(9)]
for i, row in enumerate(sudoku):
    for j, m in enumerate(row):
        if m:
            sudoku_row[i][m] = True
            sudoku_col[j][m] = True
            sudoku_sq[(i // 3) * 3 + j // 3][m] = True

solve_sudoku(0)


'''
# 시간 초과
"""
solution form 2239
스캐치
1. 각 블럭별로(3 * 3) 진행
2. 각 블럭 탐색은 while-stack 활용 dfs
3. 블럭 별 탐색 이동은 함수 dfs로
불가능한 스도쿠는 없다고 가정하고 풀이
"""
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def solve_sudoku(sudoku_sq, box_now):
    global sudoku_row, sudoku_col, sudoku_sq_num
    # 스도쿠 완성
    if box_now == 9:
        # 출력 형태로 조정
        sudoku = [[] for _ in range(9)]
        for i in range(3):
            for j in range(3):
                sudoku[i * 3 + j].extend(
                    sudoku_sq[i * 3][j] + sudoku_sq[i * 3 + 1][j] + sudoku_sq[i * 3 + 2][j]
                    )
        for line in sudoku:
            print(*line)
        # 종료
        exit()
    # 각 블럭을 탐색할 두개의 스택
    # 채워야 할 숫자
    nums_to_fill = sorted(set(range(1, 10)) - sudoku_sq_num[box_now], reverse = True)
    # 이전 장소 저장
    pos_before = []
    # 만약 채울 숫자가 없으면 바로 다음 블럭으로
    if not nums_to_fill:
        solve_sudoku(sudoku_sq, box_now + 1)
    else:
        # 지금 탐색하고 있는 장소
        pos = 0
        num = nums_to_fill[-1]
        while True:
            # pos와 스택에서 숫자를 꺼내 탐색
            # 탐색할 때, 
            # 1. pos가 9일 때, 이전 pos를 꺼내어 되돌아가서 탐색
            # 2. 해당 칸에 넣을 수 있는지 확인
            # 3. 해당 행/열에 넣을 수 있는지 확인
            # 탐색이 끝나고 수를 넣을 수 있으면
            # 1. 더 넣어야 할 숫자가 있으면 다음 숫자로 탐색
            # 2. 더 넣을 숫자가 없으면 깊이 들어가서 탐색
            if pos == 9:
                # 해당 숫자로 불가능하다는 조건
                # pos_before가 차 있으면, 이전 위치를 다른 위치로 변경하며 탐색
                # 만약 비어있다면 재귀를 얕게 보내어 다시 탐색
                if pos_before:
                    pos = pos_before.pop()
                    num = sudoku_sq[box_now][pos // 3][pos % 3]
                    sudoku_sq[box_now][pos // 3][pos % 3] = 0
                    sudoku_row[(box_now // 3) * 3 + pos // 3].remove(num)
                    sudoku_col[(box_now % 3) * 3 + pos % 3].remove(num)
                    nums_to_fill.append(num)
                    pos += 1
                else:
                    return
            elif sudoku_sq[box_now][pos // 3][pos % 3]:
                pos += 1
            elif (num in sudoku_row[(box_now // 3) * 3 + pos // 3]) or (num in sudoku_col[(box_now % 3) * 3 + pos % 3]):
                pos += 1
            else:
                # 해당 칸에 숫자를 넣을 수 있음
                sudoku_sq[box_now][pos // 3][pos % 3] = num
                nums_to_fill.pop()
                pos_before.append(pos)
                sudoku_row[(box_now // 3) * 3 + pos // 3].add(num)
                sudoku_col[(box_now % 3) * 3 + pos % 3].add(num)
                # 채워야 할 숫자가 더 남아 있는지 확인
                if not nums_to_fill:
                    solve_sudoku(sudoku_sq, box_now + 1)
                    # 재귀 돌아와서 마지막 pos_before부터 빼가면서 다른 위치 탐색
                    pos = pos_before.pop()
                    num = sudoku_sq[box_now][pos // 3][pos % 3]
                    sudoku_sq[box_now][pos // 3][pos % 3] = 0
                    sudoku_row[(box_now // 3) * 3 + pos // 3].remove(num)
                    sudoku_col[(box_now % 3) * 3 + pos % 3].remove(num)
                    nums_to_fill.append(num)
                    pos += 1
                # 채워야 할 수가 더 있으면 pos를 0으로 다시 탐색 시작
                else:
                    pos = 0
                    num = nums_to_fill[-1]


sudoku = [list(map(int, input().split())) for _ in range(9)]
# 전처리
sudoku_row = {i:set() for i in range(9)}
sudoku_col = {i:set() for i in range(9)}
sudoku_sq = {i:[[0]*3 for _ in range(3)] for i in range(9)}
sudoku_sq_num = {i:set() for i in range(9)}

for i, row in enumerate(sudoku):
    for j, m in enumerate(row):
        if m:
            sudoku_row[i].add(m)
            sudoku_col[j].add(m)
            # 박스 번호
            box_num = i // 3 * 3 + j // 3
            sudoku_sq[box_num][i % 3][j % 3] = m
            sudoku_sq_num[box_num].add(m)


solve_sudoku(sudoku_sq, 0)
'''


'''
import sys

input = lambda : sys.stdin.readline()


def check(i, j):
    global sudoku
    # 가로 확인
    tmp = [0] * 10
    zeros = 0
    for k in range(9):
        x = sudoku[i][k]
        if x != 0:
            tmp[x] = 1
        else:
            zeros += 1
    if zeros >= 2:
        next
    else:
        for k in range(1, 10):
            if tmp[k] == 0:
                sudoku[i][j] = k
                break
        return True
    # 세로 확인
    tmp = [0] * 10
    zeros = 0
    for k in range(9):
        x = sudoku[k][j]
        if x != 0:
            tmp[x] = 1
        else:
            zeros += 1
    if zeros >= 2:
        next
    else:
        for k in range(1, 10):
            if tmp[k] == 0:
                sudoku[i][j] = k
                break
        return True
    # 사각형 확인
    tmp = [0] * 10
    zeros = 0
    for k in range(3):
        for l in range(3):
            x = sudoku[i // 3 + k][j // 3 + l]
            if x != 0:
                tmp[x] = 1
            else:
                zeros += 1
    if zeros >= 2:
        next
    else:
        for k in range(1, 10):
            if tmp[k] == 0:
                sudoku[i][j] = k
                break
        return True
    # 모든 경우가 불가능할 때
    return False

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

while True:
    for point in blank:
        i, j = point
        if check(i, j):
            blank.remove(point)

for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end = ' ')
    print()
'''