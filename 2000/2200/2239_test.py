"""
Title : 스도쿠
Link : https://www.acmicpc.net/problem/2239
"""

import sys
input = sys.stdin.readline


def solve_sudoku(sudoku):
    nums = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(10)]
    # 들어 있는 숫자는 채우기
    for i, row in enumerate(sudoku):
        for j, m in enumerate(row):
            if m:
                # 3*3 기준 어디에 있는지
                x, y = i % 3, j % 3
                # 해당 블록을 위치로 배정
                nums[m][i][j] = x * 3 + y
    #







sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]



'''
# 시간초과
import sys
from itertools import product
input = sys.stdin.readline

# 각 자리별 가능한 요소를 저장
def solve_sudoku(sudoku):
    R, C = 3, 3
    n = R * C
    possible = {}
    for i, j in product(range(n), range(n)):
        possible[('row', (i, j))] = set()
        possible[('col', (i, j))] = set()
        possible[('sq', (i, j))] = set()
    for i, j, m in product(range(n), range(n), range(1, n + 1)):
        possible[('row', (i, j))].add(m)
        possible[('col', (i, j))].add(m)
        possible[('sq', (i, j))].add(m)
    
    # 스도쿠에 숫자가 있으면 제거
    for i, row in enumerate(sudoku):
        for j, m in enumerate(row):
            if m:
                # 해당 블록
                x = (i // 3) * 3
                y = (j // 3) * 3
                # 행 제거
                for k in range(9):
                    possible[('row', (i, k))].remove(m)
                for k in range(9):
                    possible[('col', (k, j))].remove(m)
                for k in range(3):
                    for l in range(3):
                        possible[('sq', (x + k, y + l))].remove(m)
    
    search(sudoku, possible, 0, 0)


def search(sudoku, possible, i, j):
    # 종료 조건
    if i == 9:
        for line in sudoku:
            print(*line, sep = '')
        quit()
    # 보고 있는 좌표 조정
    if j == 9:
        i += 1
        j = 0
        search(sudoku, possible, i, j)
    # 스도쿠 탐색
    if sudoku[i][j]:
        search(sudoku, possible, i, j + 1)
    else:
        possible_nums = possible[('row', (i, j))]\
                        & possible[('col', (i, j))]\
                        & possible[('sq', (i, j))]
        # 가능한 숫자가 없으면 돌아가기
        if not possible_nums:
            return
        # 가능한 숫자가 있으면 순서대로 탐색
        for num in sorted(possible_nums):
            sudoku[i][j] = num
            x = (i // 3) * 3
            y = (j // 3) * 3
            for k in range(9):
                possible[('row', (i, k))].remove(num)
            for k in range(9):
                possible[('col', (k, j))].remove(num)
            for k in range(3):
                for l in range(3):
                    possible[('sq', (x + k, y + l))].remove(num)
            search(sudoku, possible, i, j + 1)
            sudoku[i][j] = 0
            for k in range(9):
                possible[('row', (i, k))].add(num)
            for k in range(9):
                possible[('col', (k, j))].add(num)
            for k in range(3):
                for l in range(3):
                    possible[('sq', (x + k, y + l))].add(num)


sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]

sudoku = solve_sudoku(sudoku)
for line in sudoku:
    print(*line, sep='')
'''