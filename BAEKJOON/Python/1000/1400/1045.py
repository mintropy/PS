"""
Title : 도로
Link : https://www.acmicpc.net/problem/1045
"""

from sys import stdin

input = stdin.readline


def find_parent(parents: list, x: int) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parents(parents: list, x: int, y: int) -> list:
    if x < y:
        x, y = y, x
    parents[y] = x
    return parents


if __name__ == "__main__":
    N, M = map(int, input().split())
    roads = [input().strip() for _ in range(N)]
    roads_sets = []
    unused = []
    parents = list(range(N))
    for i in range(N):
        for j in range(i + 1, N):
            if roads[i][j] == "N":
                continue
            x, y = find_parent(parents, i), find_parent(parents, j)
            if x == y:
                unused.append((i, j))
                continue
            roads_sets.append((i, j))
            parents = union_parents(parents, x, y)
    if len(roads_sets) < N - 1 or len(roads_sets + unused) < M:
        print(-1)
    else:
        ans = [0] * N
        for x, y in roads_sets:
            ans[x] += 1
            ans[y] += 1
        for i in range(M - (N - 1)):
            x, y = unused[i]
            ans[x] += 1
            ans[y] += 1
        print(*ans)

"""
0 ~ N-1 : N개 도시
두 도시를 연결하는 도로
    도로 우선순위,
    (A, B) 도로 x, (C, D) 도로 y
    (A, B) < (C, D) 이면 x의 우선순위 높음
M개 도로를 가진 도로의 집합 중 장 높은 우선순위

조건
도시가 연결되어 있어야함
도로 우선 순위가 가장 높아야 함
"""
