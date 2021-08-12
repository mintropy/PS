"""
Title : 불켜기
Link : https://www.acmicpc.net/problem/11967
"""

import sys, collections
input = sys.stdin.readline


n, m = map(int, input().split())
switch = collections.defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switch[(x, y)].append((a, b))

lights = [[False] * (n + 2) for _ in range(n + 2)]
lights[1][1] = True
# visited = [[False] * (n + 2) for _ in range(n + 2)]
# visited[1][1] = True
room_count = 1

queue = collections.deque([(1, 1)])

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while queue:
    x, y = queue.popleft()
    # 해당 방에서 모든 불 켜기
    for x2, y2 in switch[(x, y)]:
        if not lights[x2][y2]:
            lights[x2][y2] = True
            room_count += 1
            # 움직일 수 있는 방 확인
            # 불을 새로 켜고, 기존 불켜진 방과 이어져 있으면 queue 추가
            for d in range(4):
                nx, ny = x2 + dx[d], y2 + dy[d]
                if lights[nx][ny]:
                    queue.append((x2, y2))
                    queue.append((nx, ny))

print(room_count)
