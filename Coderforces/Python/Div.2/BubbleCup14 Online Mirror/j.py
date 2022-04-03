import collections
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

factory = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
rooms = []
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_count = 0
            queue = collections.deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                room_count += 1
                for d in range(4):
                    # No Wall
                    if not (factory[x][y] & (1 << d)):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            queue.append((nx, ny))
            rooms.append(room_count)

print(*sorted(rooms, reverse=True))
