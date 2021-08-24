# Title : 마법사 상어와 비바라기
# Link : https://www.acmicpc.net/problem/21610


import sys

input = sys.stdin.readline

def move_cloud(cloud: list, direction: int, time: int) -> list:
    global n, dx, dy
    for j in range(len(cloud)):
        x, y = cloud[j]
        nx, ny = x + dx[direction] * time, y + dy[direction] * time
        nx, ny = (nx + n) % n, (ny + n) % n
        cloud[j] = [nx, ny]
    return cloud

def rain(cloud: list) -> list:
    global graph, n, dx, dy
    for x, y in cloud:
        graph[x][y] += 1
    # 물복사 버그
    count = [0] * len(cloud)
    for i in range(len(cloud)):
        x, y = cloud[i]
        for j in range(4):
            nx, ny = x + dx[2 * j + 1], y + dy[2 * j + 1]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= 1:
                    count[i] += 1
    for i in range(len(cloud)):
        graph[cloud[i][0]][cloud[i][1]] += count[i]
    # 다음 구름
    next_cloud = []
    for i in range(n):
        for j in range(n):
            if [i, j] in cloud:
                continue
            if graph[i][j] >= 2:
                next_cloud.append([i, j])
                graph[i][j] -= 2
    return next_cloud


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cmd = [list(map(int, input().split())) for _ in range(m)]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for d, t in cmd:
    cloud = move_cloud(cloud, d - 1, t)
    cloud = rain(cloud)

answer = 0
for i in range(n):
    answer += sum(graph[i])
print(answer)