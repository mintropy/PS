"""
Title : 임계경로
Link : https://www.acmicpc.net/problem/1948
"""

from collections import deque
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    roads = [[] for _ in range(N + 1)]
    in_roads = [0] * (N + 1)
    for _ in range(M):
        s, e, t = MIIS()
        roads[s].append((e, t))
        in_roads[e] += 1
    st, end = MIIS()

    time = [0] * (N + 1)
    parent = [[] for _ in range(N + 1)]
    queue = deque([(st, 0)])
    while queue:
        x, t = queue.popleft()
        for y, _t in roads[x]:
            in_roads[y] -= 1
            next_time = t + _t
            if time[y] == next_time:
                parent[y].append(x)
            if time[y] < next_time:
                time[y] = next_time
                parent[y] = [x]
            if not in_roads[y]:
                queue.append((y, time[y]))

    roads_count = set()
    queue = deque([end])
    while queue:
        x = queue.popleft()
        for y in parent[x]:
            if (y, x) in roads_count:
                continue
            roads_count.add((y, x))
            if y != st:
                queue.append(y)

    print(time[end])
    print(len(list(roads_count)))

"""
5
7
1 2 1
1 3 3
2 3 2
2 4 1
2 5 3
3 5 1
4 5 1
1 5
ans : 4 5
"""
