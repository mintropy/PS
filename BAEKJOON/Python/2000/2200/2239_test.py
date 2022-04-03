"""
Title : 스도쿠
Link : https://www.acmicpc.net/problem/2239
"""

# https://www.acmicpc.net/source/18433291
path = []
n, m = 9, 81
rows = [{*range(j, j+n)} for j in range(0, m, n)]
cols = [{*range(i, m, n)} for i in range(n)]
square = [0, 1, 2, 9, 10, 11, 18, 19, 20]
square33s = []
for i in range(0, m, 27):
    for j in range(0, n, 3):
        k = i + j
        square33s.append({k + a for a in square})

import sys
input = sys.stdin.readline
for i in range(n):
    for j in range(n):
        path.append(rows[i].union(cols[j], square33s[j // 3 + i - i % 3])) # path[i*n+j]: ith row, jth col
        path[i*n+j].remove(i*n+j)
path2 = [[] for _ in range(m)]

bits = [1 << i for i in range(n)]
whole = (1 << n) - 1
tobit = lambda i: 1 << (i - 1) if i else whole
tobit2 = lambda i: 1 << (i - 1) if i else 0
tonum = {1 << i: i + 1 for i in range(9)}
tonum[0] = 0
option = []
current = []

for _ in range(n):
    new = list(map(int, input().rstrip()))
    option += [*map(tobit, new)]
    current += [*map(tobit2, new)]
zeroes, nonzeroes = [], set()
for i, j in enumerate(current):
    if not j:
        zeroes.append(i)

def compute_avail(zeroes):
    new_zeroes = []
    for i in zeroes:
        x = option[i]
        a = 0
        for y in path[i]:
            new = current[y]
            if new:
                a |= new
            elif y > i:
                path2[i].append(y)
        path[i].difference_update(path2[i], nonzeroes)
        x &= ~a
        assert x != 0
        if x in tonum:
            current[i] = x
        option[i] = x
    # Do it once more, insert it in reversed order
    for i in zeroes[::-1]:
        x = option[i]
        if x == current[i]:
            continue
        a = 0
        for y in path2[i]:
            a |= current[y]
        x &= ~a
        assert x != 0
        if x in tonum:
            current[i] = x
        else:
            new_zeroes.append(i)
        option[i] = x
    return new_zeroes

def check_unique(change, t = False):
    if t:
        for i in range(n):
            print(*[tonum[j] for j in current[i * n:(i + 1) * n]], sep = '')

        print('=' * 9)

    for row in rows:
        for bit in bits:
            tmp = [i for i in row if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    for col in cols:
        for bit in bits:
            tmp = [i for i in col if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    for sq in square33s:
        for bit in bits:
            tmp = [i for i in sq if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    if t:
        for i in range(n):
            print(*[tonum[j] for j in current[i * n:(i + 1) * n]], sep = '')
        print('='*9)
    return change
def dfs(index):
    if index == -1:
        for i in range(n):
            print(*[tonum[j] for j in current[i*n:(i+1)*n]], sep = '')
        sys.exit()
        return

    u = zeroes[index]
    val = option[u]
    anti = 0
    for j in path[u]:
        anti |= current[j]
    val &= ~anti
    index -= 1
    for bit in bits:
        if bit & val:
            current[u] = bit
            dfs(index)
    current[u] = 0

zeroes = compute_avail(zeroes)
zeroes = check_unique(zeroes)[::-1]
zeroes = compute_avail(zeroes)


dfs(len(zeroes) - 1)


"""
스캐치
1. 각 블럭별로(3 * 3) 진행
2. 각 블럭 탐색은 while-stack 활용 dfs
3. 블럭 별 탐색 이동은 함수 dfs로
불가능한 스도쿠는 없다고 가정하고 풀이
"""

'''
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
            print(*line, sep = '')
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


sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]
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