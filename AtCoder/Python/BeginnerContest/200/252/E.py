import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_pa(pa, x):
    while x != pa[x]:
        x = pa[x]
    return x


def union_pa(pa, x, y):
    if x > y:
        x, y = y, x
    pa[y] = x
    return parents


N, M = MIIS()
roads = [[tuple(MIIS()), idx] for idx in range(1, N + 1)]
roads.sort(key=lambda x: x[0][2])

parents = list(range(N + 1))
ans = []
for (a, b, c), idx in roads:
    a, b = find_pa(parents, a), find_pa(parents, b)
    if a == b:
        continue
    ans.append(idx)
    parents = union_pa(parents, a, b)

print(*ans)

'''
import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
roads = [[] for _ in range(N + 1)]
heap = []
for i in range(M):
    A, B, C = MIIS()
    roads[A].append((i + 1, B, C))
    roads[B].append((i + 1, A, C))
    if A == 1:
        heap.append((C, B, i + 1))
    if B == 1:
        heap.append((C, A, i + 1))
heapq.heapify(heap)

dists = [0] * (N + 1)
ans_roads = set()
while heap and len(ans_roads) < N - 1:
    next_dist, next_city, idx = heapq.heappop(heap)
    if dists[next_city] or idx in ans_roads:
        continue
    dists[next_city] = next_dist
    ans_roads.add(idx)
    for _idx, _next_city, _next_dist in roads[next_city]:
        if dists[_next_city]:
            continue
        heapq.heappush(heap, (next_dist + _next_dist, _next_city, _idx))

print(*ans_roads)
'''