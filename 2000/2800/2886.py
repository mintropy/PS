"""
Title : 자리 전쟁
Link : https://www.acmicpc.net/problem/2886
"""

import sys, heapq
input = sys.stdin.readline


def bfs(i, j):
    global r, c, train, dx, dy
    heap = [(0, i, j)]
    visited = [[False] * c for _ in range(r)]
    person_dist = 10 ** 6
    person = []
    while heap:
        dist, x, y = heapq.heappop(heap)
        # 사람인지 확인 확인
        if train[x][y] == 'X':
            # 지금까지 찾은 사람 최소거리보다 짧으면 종료
            if dist > person_dist:
                break
            # 더 짧은 거리는 없고
            # 같은 거리 사람이 있으면 아무것도 하지 않고 종료
            elif dist == person_dist:
                return
            else:
                person_dist = dist
                person = [x, y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(heap, ((i - nx) ** 2 + (j - ny) ** 2, nx, ny))
    # 가까운 사람이 있는지 확인하고 있으면
    # 종료 전 사람과 좌석 삭제
    if person:
        train[i][j] = '.'
        train[person[0]][person[1]] = '.'


r, c = map(int, input().split())
train = [list(input().strip()) for _ in range(r)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 좌석을 찾으면 가장 가까운 사람을 찾아서 짝지어 제거
# 만약 거리가 같은 사람이 둘 이상이면 그대로 두고 한번 더 탐색
for _ in range(2):
    for i in range(r):
        for j in range(c):
            if train[i][j] == 'L':
                bfs(i, j)

# 남은 좌석 확인
seat_count = 0
for i in range(r):
    for j in range(c):
        if train[i][j] == 'L':
            seat_count += 1

print(seat_count)