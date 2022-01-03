"""
Title : 생물학자
Link : https://www.acmicpc.net/problem/3116
"""

import sys
input = sys.stdin.readline


def is_encounter(x1, y1, d1, x2, y2, d2) -> tuple:
    global dx, dy
    diff_dx = dx[d1] - dx[d2]
    diff_dy = dy[d1] - dy[d2]
    if diff_dx == 0 and diff_dy == 0:
        return (False, 0)
    if diff_dx == 0 and y1 != y2:
        return (False, 0)
    if diff_dy == 0 and x1 != x2:
        return (False, 0)
    if diff_dx == 0:
        if (y1 - y2) % diff_dy != 0:
            return (False, 0)
        else:
            return (True, (y1 - y2) // diff_dy)
    if diff_dy == 0:
        if (x1 - x2) % diff_dx != 0:
            return (False, 0)
        else:
            return (True, (x1 - x2) // diff_dx)
    if (x1 - x2) % diff_dx != 0 or (y1 - y2) % diff_dy != 0:
        return (False, 0)
    if abs((x1 - x2) % diff_dx) != abs((y1 - y2) % diff_dy != 0):
        return (False, 0)
    return (True, (x1 - x2) // diff_dx)


N = int(input())
bacterias = [tuple(map(int, input().split())) for _ in range(N)]

dx, dy = (0, -1, -1, -1, 0, 1, 1, 1, 0), (0, -1, 0, 1, 1, 1, 0, -1, -1)
encounters = {}
for i in range(N):
    x1, y1, d1 = bacterias[i]
    for j in range(i + 1, N):
        x2, y2, d2 = bacterias[j]
        b, t =  is_encounter(x1, y1, d1, x2, y2, d2)
        if b:
            if t in encounters:
                encounters[t].append((i, j))
            else:
                encounters[t] = [(i, j)]

max_count = 0
time = 0
for time_now, encounter in encounters.items():
    count = {}
    for i, j in encounter:
        if i in count:
            count[i] += 1
        else:
            count[i] = 2
        if j in count:
            count[j] += 1
        else:
            count[j] = 2
    tmp = max(count.values())
    if max_count < tmp:
        max_count = tmp
        time = time_now

print(max_count)
print(time)
