import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    h, w = map(int, input().split())
    hall = [[0 for _ in range(w)] for _ in range(h)]
    # upper line
    for i in range(0, w, 2):
        hall[0][i] = 1
    # right line
    if hall[0][-2] == 1:
        for i in range(2, h, 2):
            hall[i][-1] = 1
    else:
        for i in  range(0, h, 2):
            hall[i][-1] = 1
    # lower line
    if hall[-2][-1] == 1:
        for i in range(2, w, 2):
            hall[-1][-1 -i] = 1
    else:
        for i in  range(0, w, 2):
            hall[-1][-1 -i] = 1
    # left line
    if hall[-1][1] == 1:
        for i in range(2, h, 2):
            hall[-1 -i][0] = 1
    else:
        for i in  range(0, h, 2):
            hall[-1 -i][0] = 1

    # check
    hall[1][0] = 0

    for i in range(h):
        for j in range(w):
            print(hall[i][j], end ='')
        print()