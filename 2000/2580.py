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