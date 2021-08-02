"""
Title : 오목
Link : https://www.acmicpc.net/problem/2072
"""

import sys
input = sys.stdin.readline


def check_omok(omok: list, color: int, i: int, j :int) -> bool:
    direction = {
        0: [(-1, 0), (1, 0)],
        1: [(-1, 1), (1, -1,)],
        2: [(0, 1), (0, -1)],
        3: [(1, 1), (-1, -1)]
    }
    # 네 방향으로 확인
    for d in range(4):
        d1, d2 = direction[d]
        count = 1
        for k in range(1, 6):
            x, y = i + d1[0] * k, j + d1[1] * k
            if omok[x][y] == color:
                count += 1
            else:
                break
        for k in range(1, 6):
            x, y = i + d2[0] * k, j + d2[1] * k
            if omok[x][y] == color:
                count += 1
            else:
                break
        if count == 5:
            return True
    return False



n = int(input())

omok = [[0 for _ in range(21)] for _ in range(21)]

# 흑 >> 백 순서
# 빈칸은 0, 흑은 1, 백은 2로 표시
for i in range(1, n + 1):
    a, b = map(int, input().split())
    if i % 2 == 1:
        color = 1
    else:
        color = 2
    omok[a][b] = color
    if check_omok(omok, color, a, b):
        print(i)
        break
else:
    print(-1)