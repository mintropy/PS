from sys import stdin
from collections import deque


# 미로 가로, 세로 크기
m, n = map(int, stdin.readline().split())

# 미로 상태, 0은 빈방, 1은 벽
maze = []
for _ in range(n):
    num = str(stdin.readline())
    tmp = []
    for i in range(m):
        tmp.appned(int(num[i]))
    maze.append(tmp)


m, n = 3, 3
maze = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]

m, n = 4, 2
maze = [[0,0,0,1], [1,0,0,0]]

m, n = 6, 6
maze = [[0,0,1,1,1,1],[0,1,0,0,0,0],[0,0,1,1,1,1],
        [1,1,0,0,0,1],[0,1,1,0,1,0],[1,0,0,0,1,0]]


def bfs(maze):
    global m, n
    # 부순 벽의 개수, 위치
    queue = deque([(0, 0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        d, x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(d)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if maze[nx][ny] == 0:
                queue.appendleft((d, nx, ny))
                visited[nx][ny] = True
            elif maze[nx][ny] == 1:
                queue.append((d + 1, nx, ny))
                visited[nx][ny] = True

bfs(maze)