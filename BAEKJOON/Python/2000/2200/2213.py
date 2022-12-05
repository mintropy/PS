"""
Title : 트리의 독립집합
Link : https://www.acmicpc.net/problem/2213
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search(now: int, parent: int):
    global N, weights, tree, dp
    dp[now][1] = weights[now - 1]
    for x in tree[now]:
        if x == parent:
            continue
        search(x, now)
        dp[now][0] += max(dp[x])
        dp[now][1] += dp[x][0]


def get_nodes(now: int, parent: int, include: bool) -> list[int]:
    global tree, dp
    tmp = []
    if include:
        tmp.append(now)
        for x in tree[now]:
            if x == parent:
                continue
            tmp += get_nodes(x, now, False)
    else:
        for x in tree[now]:
            if x == parent:
                continue
            if dp[x][0] < dp[x][1]:
                tmp += get_nodes(x, now, True)
            else:
                tmp += get_nodes(x, now, False)
    return tmp


if __name__ == "__main__":
    N = int(input())
    weights = tuple(MIIS())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = MIIS()
        tree[x].append(y)
        tree[y].append(x)
    dp = [[0] * 2 for _ in range(N + 1)]
    search(1, 0)
    print(max(dp[1]))
    print(*sorted(get_nodes(1, 0, True if dp[0] < dp[1] else False)))
