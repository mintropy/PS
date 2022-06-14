"""
Title : 수들의 합 7
Link : https://www.acmicpc.net/problem/2268
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.seq = [0] * (N + 1)
        self.tree = [0] * (1 << (ceil(log2(N)) + 1))

    def find_sum(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.find_sum(node * 2, start, mid, left, right) + self.find_sum(
            node * 2 + 1, mid + 1, end, left, right
        )

    def update(self, node: int, start: int, end: int, index: int, diff: int) -> None:
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        self.update(node * 2, start, mid, index, diff)
        self.update(node * 2 + 1, mid + 1, end, index, diff)


if __name__ == "__main__":
    N, M = MIIS()
    segment_tree = SegmentTree(N)
    for _ in range(M):
        cmd, x, y = MIIS()
        if not cmd:
            if x > y:
                x, y = y, x
            print(segment_tree.find_sum(1, 0, N - 1, x, y))
        else:
            segment_tree.update(1, 0, N - 1, x, y - segment_tree.seq[x])
