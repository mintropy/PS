"""
Title : 소문난 칠공주
Link : https://www.acmicpc.net/problem/1941
"""

import sys
input = sys.stdin.readline


def dfs(seven_princess_now: set, possible_seat: set, som_pa_now: int):
    global students, students_check, possible_seven_princess, dx, dy
    if 7 - len(seven_princess_now) + som_pa_now < 4:
        return
    if len(seven_princess_now) == 7:
        if som_pa_now >= 4:
            possible_seven_princess.add(tuple(sorted(seven_princess_now)))
        return
    for x, y in possible_seat:
        if students_check[x][y]:
            continue
        tmp_seat = set()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5:
                tmp_seat.add((nx, ny))
        students_check[x][y] = True
        if students[x][y] == 'S':
            dfs(seven_princess_now | {(x, y)}, (possible_seat | tmp_seat) - {(x, y)}, som_pa_now + 1)
        else:
            dfs(seven_princess_now | {(x, y)}, (possible_seat | tmp_seat) - {(x, y)}, som_pa_now)
        students_check[x][y] = False


students = [input().strip() for _ in range(5)]
students_check = [[False] * 5 for _ in range(5)]

possible_seven_princess = set()
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

for i in range(5):
    for j in range(5):
        if students[i][j] == 'S':
            possible_seat = set()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < 5 and 0 <= nj < 5:
                    possible_seat.add((ni, nj))
            students_check[i][j] = True
            dfs({(i, j)}, possible_seat, 1)
            students_check[i][j] = False

print(len(possible_seven_princess))


'''
Counter Example
SSYYY
SYYYY
YYSYY
YYYYY
YYYYY
ans : 23
'''