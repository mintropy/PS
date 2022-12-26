"""
Title : 오민식의 고민
Link : https://www.acmicpc.net/problem/1219
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def bellman_ford(
    N: int, st: int, end: int, transfers: list[tuple[int]], cities: list[int]
):
    INF = 100_000_000
    dist = [INF] * N
    dist[st] = -cities[st]
    for _ in range(N - 1):
        for cur_node, next_node, cost in transfers:
            if dist[cur_node] != INF and dist[next_node] > (
                next_cost := dist[cur_node] + cost - cities[next_node]
            ):
                dist[next_node] = next_cost
    if dist[end] == INF:
        return "gg"
    for cur_node, next_node, cost in transfers:
        if (
            dist[cur_node] != INF
            and dist[next_node] > dist[cur_node] + cost - cities[next_node]
        ):
            return "Gee"
    return -dist[end]


if __name__ == "__main__":
    N, st, end, M = MIIS()
    transfers = [tuple(MIIS()) for _ in range(M)]
    cities = list(MIIS())
    print(bellman_ford(N, st, end, transfers, cities))
