"""
Title : 화산 쇄설류
Link : https://www.acmicpc.net/problem/16569
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == '__main__':
    M, N, V = MIIS()
    X, Y = MIIS()
    heights = [[0 for _ in range(N + 1)]] + [[0] + list(MIIS()) for _ in range(M)]
    dusts = sorted([list(MIIS()) for _ in range(V)], key=lambda x: x[2])
    volcano = {(x, y) for x, y, _ in dusts}
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

    dusts_now = []
    possible_pos = [(X, Y)]
    max_heights = heights[X][Y]
    ans_time = 0
    idx = 0
    time_now = 0
    while idx < V:
        x, y, t = dusts[idx]
        if t == 0:
            heights[x][y] = -1
            dusts_now.append((x, y))
        else:
            break
    heights[X][Y] = -1
    
    while possible_pos:
        if idx == V:
            next_time = 10000
        else:
            next_time = dusts[idx][2] - time_now
        for _ in range(next_time):
            time_now += 1
            next_pos = []
            dust_next = []
            for x, y in dusts_now:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 1 <= nx <= M and 1 <= ny <= N and heights[nx][ny] >= 0:
                        heights[nx][ny] = -1
                        dust_next.append((nx, ny))
            for x, y in possible_pos:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx, ny) in volcano:
                        continue
                    if 1 <= nx <= M and 1 <= ny <= N and heights[nx][ny] >= 0:
                        if max_heights < heights[nx][ny]:
                            max_heights = heights[nx][ny]
                            ans_time = time_now
                        heights[nx][ny] = -1
                        next_pos.append((nx, ny))
            dusts_now = dust_next[::]
            possible_pos = next_pos[::]
        while idx < V:
            if dusts[idx][2] == time_now:
                x, y, _ = dusts[idx]
                dusts_now.append((x, y))
                idx += 1
            else:
                break
    print(max_heights, ans_time)

'''
Count Example
3 3 2
3 1
1000 0 0
0 0 0
0 0 0
2 1 100
2 2 100
ans : 1000 6
'''
