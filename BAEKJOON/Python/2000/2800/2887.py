"""
Title : 행성 터널
Link : https://www.acmicpc.net/problem/2887
"""

import sys
input = sys.stdin.readline


def find_parent(a: int, parent: list) -> int:
    # a의 부모 찾아서 리턴
    while a != parent[a]:
        a = parent[a]
    return a


def union_parendt(a: int, b: int, parent: list):
    a, b = find_parent(a, parent), find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
# 입력을 각 좌표별로 받아서 정렬
planets_x = []
planets_y = []
planets_z = []
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    planets_x.append((x, i))
    planets_y.append((y, i))
    planets_z.append((z, i))
planets_x.sort()
planets_y.sort()
planets_z.sort()

# 좌표 차이가 가장 적은 행성 사이 연결
dist = []
for i in range(n - 1):
    # x좌표
    x1, a = planets_x[i]
    x2, b = planets_x[i + 1]
    dist.append((x2 - x1, a, b))
    # y좌표
    y1, a = planets_y[i]
    y2, b = planets_y[i + 1]
    dist.append((y2 - y1, a, b))
    # z좌표
    z1, a = planets_z[i]
    z2, b = planets_z[i + 1]
    dist.append((z2 - z1, a, b))
dist.sort()

visited = [False] * (n + 1)
total_dist = 0
edges_count = 0
parents = [i for i in range(n + 1)]
for d, a, b in dist:
    if edges_count == n - 1:
        break
    # 두 점의 부모 확인
    # 두 점의 부모가 다르면 union
    if find_parent(a, parents) != find_parent(b, parents):
        union_parendt(a, b, parents)
        total_dist += d
        edges_count += 1

print(total_dist)
