"""
Title : 트리의 독립집합
Link : https://www.acmicpc.net/problem/2213
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def solve(N: int, weights: tuple[int], tree: list[set[int]]) -> list[int]:
    max_weight = [[0] * 4 for _ in range(N + 1)]
    for i, w in enumerate(weights):
        max_weight[i + 1][0] = w
        max_weight[i + 1][2] = i + 1
    leaves = deque([x for x in range(1, N + 1) if len(tree[x]) == 1])

    ans = []
    while leaves:
        x = leaves.popleft()
        if not tree[x]:
            ans.append(max(max_weight[x]))
            break
        y = tree[x].pop()
        w = weights[y - 1]

        if (tmp := w + max_weight[x][1]) > max_weight[y][0]:
            max_weight[y][0] = tmp
            max_weight[y][2] = max_weight[x][3]
        if (tmp := max(max_weight[x][:2])) > max_weight[y][1]:
            max_weight[y][1] = tmp
            if max_weight[x][0] > max_weight[x][1]:
                max_weight[y][3] = x
            else:
                max_weight[y][3] = max_weight[x][3]
        tree[y].remove(x)
        if len(tree[y]) == 1:
            leaves.append(y)
    x = ans[0]


if __name__ == "__main__":
    N = int(input())
    weights = tuple(MIIS())
    tree = [set() for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = MIIS()
        tree[x].add(y)
        tree[y].add(x)
    ans = solve(N, weights, tree)
    print(ans[0])
    print(*ans[1:])
