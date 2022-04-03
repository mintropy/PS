"""
Title : 배열 돌리기 1
Link : https://www.acmicpc.net/problem/16926
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def rotate(array, pos, r):
    tmp = []
    # 반시계 방향으로 저장
    for i in range(pos, n - pos):
        tmp.append(array[i][pos])
    for i in range(pos + 1, m - pos):
        tmp.append(array[n - 1 - pos][i])
    for i in range(n - 1 - pos - 1, pos - 1, -1):
        tmp.append(array[i][m - 1 - pos])
    for i in range(m - 1 - pos - 1, pos, -1):
        tmp.append(array[pos][i])
    # r개 후의 것을 뽑아서 다시 순회하며 입력
    idx = (0 - r) % len(tmp)
    for i in range(pos, n - pos):
        array[i][pos] = tmp[idx]
        idx = (idx + 1) % len(tmp)
    for i in range(pos + 1, m - pos):
        array[n - 1 - pos][i] = tmp[idx]
        idx = (idx + 1) % len(tmp)
    for i in range(n - 1 - pos - 1, pos - 1, -1):
        array[i][m - 1 - pos] = tmp[idx]
        idx = (idx + 1) % len(tmp)
    for i in range(m - 1 - pos - 1, pos, -1):
        array[pos][i] = tmp[idx]
        idx = (idx + 1) % len(tmp)    
    return array


n, m, r = MIIS()
array = [list(MIIS()) for _ in range(n)]

for i in range(min(n // 2, m // 2)):
    # 한 바퀴 기준 개수
    points = 0
    # 세로로 개수
    points += (n - i * 2) * 2
    # 가로로 개수
    points += (m - (i + 1) * 2) * 2
    # 여러번 회전하지 않도록 회수 계산
    points = r % points
    rotate(array, i, points)

for line in array:
    print(*line)
