import sys

input = sys.stdin.readline

h, w, c = map(int, input().split())
stations = [list(map(int, input().split())) for _ in range(h)]

# 시간 초과
def find(i: int, j: int, dist: int) -> list:
    '''
    i, j부터 dist거리 떨어진 점들 찾기
    '''
    possible = []
    x, y = i, j - dist
    for _ in range(dist):
        if 0 <= x < h and 0 <= y < w:
            possible.append((x, y))
        x += 1
        y += 1
    for _ in range(dist):
        if 0 <= x < h and 0 <= y < w:
            possible.append((x, y))
        x -= 1
        y += 1
    for _ in range(dist):
        if 0 <= x < h and 0 <= y < w:
            possible.append((x, y))
        x -= 1
        y -= 1
    for _ in range(dist):
        if 0 <= x < h and 0 <= y < w:
            possible.append((x, y))
        x += 1
        y -= 1
    return possible


lowest_cost = int(1e14)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
for i in range(h):
    for j in range(w):
        dist = 1
        while True:
            dist_cost = dist * c
            if dist_cost > lowest_cost:
                break
            possible = find(i, j, dist)
            if possible == []:
                break
            for x, y in possible:
                cost = dist_cost + stations[i][j] + stations[x][y]
                if cost < lowest_cost:
                    lowest_cost = cost
            dist += 1

print(lowest_cost)

'''
# 시간 초과
lowest_cost = int(1e14)
for i in range(1, h * w):
    for j in range(i + 1, h * w + 1):
        if i % w == 0:
            x1 = i // w - 1
            y1 = w - 1
        else:
            x1 = i // w
            y1 = i % w - 1
        if j % w == 0:
            x2 = j // w - 1
            y2 = w - 1
        else:
            x2 = j // w
            y2 = j % w - 1
        # 가격 계산
        cost = stations[x1][y1] + stations[x2][y2]
        cost += c * (abs(x1 - x2) + abs(y1 - y2))
        # 가격 비교
        if cost < lowest_cost:
            lowest_cost = cost
print(lowest_cost)
'''