"""
Title : 수열과 쿼리 17
Link : https://www.acmicpc.net/problem/14438
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int, seq: list[int]) -> None:
        self.N = N
        self.seq = [0] + seq
        tree_size = 1 << (ceil(log2(N)) + 1)
        self.tree = [0] * tree_size
        self.tree_idx = [0] * (N + 1)
        self.init_tree(1, 1, N)

    def mid(self, start: int, end: int) -> int:
        return (start + end) // 2

    def init_tree(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.seq[start]
            self.tree_idx[start] = node
            return
        mid = self.mid(start, end)
        self.init_tree(node * 2, start, mid)
        self.init_tree(node * 2 + 1, mid + 1, end)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, node: int, value: int) -> None:
        node = self.tree_idx[node]
        self.tree[node] = value
        node //= 2
        while node:
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])
            node //= 2

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 10**9
        if left <= start and end <= right:
            return self.tree[node]
        mid = self.mid(start, end)
        left_value = self.query(node * 2, start, mid, left, right)
        right_value = self.query(node * 2 + 1, mid + 1, end, left, right)
        return min(left_value, right_value)


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree(N, seq)
    for _ in range(II()):
        cmd, x, y = MIIS()
        if cmd == 1:
            segment_tree.update(x, y)
        elif cmd == 2:
            print(segment_tree.query(1, 1, N, x, y))
