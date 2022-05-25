"""
Title : 촌수계산
Link : https://www.acmicpc.net/problem/2644
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = int(input())
    X, Y = MIIS()
    M = int(input())
    relations = [[] for _ in range(N + 1)]
    for _ in range(M):
        _x, _y = MIIS()
        relations[_x].append(_y)
        relations[_y].append(_x)
    queue = deque([(X, 0)])
    visited = [False] * (N + 1)
    ans = -1
    while queue:
        x, d = queue.popleft()
        if x == Y:
            ans = d
            break
        if visited[x]:
            break
        visited[x] = True
        for y in relations[x]:
            if not visited[y]:
                queue.append((y, d + 1))
    print(ans)
