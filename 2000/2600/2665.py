"""
Title : 미로만들기
Link : https://www.acmicpc.net/problem/2665
"""

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
maze = [list(input()) for _ in range(N)]

if N == 1:
    print(0)
else:
    visited = [[N * N] * N for _ in range(N)]
    queue = deque([(0, 0, 0)])
    
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while queue:
        x, y, count = queue.popleft()
        if x == N - 1 and y == N - 1:
            print(count)
            break
        if visited[x][y] <= count:
            continue
        visited[x][y] = count
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == '1':
                    queue.appendleft((nx, ny, count))
                else:
                    queue.append((nx, ny, count + 1))
