"""
Title : 방탈출
Link : https://www.acmicpc.net/problem/23352
"""

from  collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
rooms = [list(MIIS()) for _ in range(N)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
total_max_len = -1
answer = 0
ans = []
for i in range(N):
    for j in range(M):
        if rooms[i][j] == 0:
            continue
        first = last = rooms[i][j]
        max_len = 0
        visitied = [[False] * M  for _ in range(N)]
        queue = deque([(i, j, 0)])
        while queue:
            x, y, l = queue.popleft()
            if visitied[x][y]:
                continue
            if l > max_len:
                max_len = l
                last = rooms[x][y]
            elif l == max_len and y > last:
                last = y
            visitied[x][y] = True
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visitied[nx][ny] and rooms[nx][ny]:
                    queue.append((nx, ny, l + 1))
        if max_len > total_max_len:
            total_max_len = max_len
            answer = first + last
            ans = [first, last]
        elif max_len == total_max_len and answer < first + last:
            answer = first + last
            ans = [first, last]

print(answer)
