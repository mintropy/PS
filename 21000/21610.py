'''
Title : 마법사 상어와 비바라기
Link : https://www.acmicpc.net/problem/21610
'''

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def cloud_move(clouds: list, d: int, s: int):
    global n, dx, dy
    for i in range(len(clouds)):
        x, y = clouds[i]
        x = (x + dx[d] * s) % n
        y = (y + dy[d] * s) % n
        clouds[i] = [x, y]


def cloud_rain(magical_bucket: list, clouds: list):
    for x, y in clouds:
        magical_bucket[x][y] += 1


def water_copy_bug(magical_bucket: list, clouds: list):
    global n, dia_dx, dia_dy
    # 원래 구름이 있는 자리에서 탐색 시작
    for x, y in clouds:
        # 각 자리에서 대각선에 물이 있는 바구니 수
        water_bucket = 0
        for d in range(4):
            nx, ny = x + dia_dx[d], y + dia_dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if magical_bucket[nx][ny] >= 1:
                    water_bucket += 1
        # 지금 자리에 물복사
        magical_bucket[x][y] += water_bucket


def water_to_cloud(magical_bucket: list, clouds: list) -> list:
    global n
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if magical_bucket[i][j] >= 2 and [i, j] not in clouds:
                new_clouds.append([i, j])
                magical_bucket[i][j] -= 2
    return new_clouds



n, m = map(int, input().split())
magical_bucket = [list(map(int, input().split())) for _ in range(n)]

clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
dx, dy = (0, 0, -1, -1, -1, 0, 1, 1, 1), (0, -1, -1, 0, 1, 1, 1, 0, -1)
dia_dx, dia_dy = (-1, -1, 1, 1), (-1, 1, 1, -1)
for _ in range(m):
    d, s = map(int, input().split())
    # 구름 이동
    cloud_move(clouds, d, s)
    # 비 내리기
    cloud_rain(magical_bucket, clouds)
    # 비 내리는 칸에서 물복사 버그
    water_copy_bug(magical_bucket, clouds)
    # 물 양이 2인 공간에서 구름 생성
    clouds = water_to_cloud(magical_bucket, clouds)

print(sum(sum(magical_bucket, start=[])))


'''
# TLE
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
'''
