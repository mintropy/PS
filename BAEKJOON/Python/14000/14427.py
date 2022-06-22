"""
Title : 수열과 쿼리 15
Link : https://www.acmicpc.net/problem/14427
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int, seq: list[int]) -> None:
        self.N = N
        self.seq = seq
        self.tree = [0] * (1 << (ceil(log2(N)) + 1))
        self.tree_idx = [0] * (N + 1)
        self.find_tree_idx(1, 1, self.N)
        self.init_tree()

    def find_tree_idx(self, node: int, left: int, right: int) -> None:
        if left >= right:
            self.tree_idx[left] = node
            return
        mid = (left + right) // 2
        self.find_tree_idx(node * 2, left, mid)
        self.find_tree_idx(node * 2 + 1, mid + 1, right)

    def init_tree(self) -> None:
        for i, x in enumerate(self.tree_idx):
            self.tree[x] = self.seq[i]

    def find_sum(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        l_sum = self.find_sum(node * 2, start, mid, left, right)
        r_sum = self.find_sum(node * 2 + 1, mid + 1, end, left, right)
        return l_sum + r_sum

    def update(self, node: int, value: int) -> None:
        node = self.tree_idx[node]
        self.tree[node] = value
        node //= 2
        while node:
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
            node //= 2


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree()
    for _ in range(II()):
        cmd, *nums = MIIS()
        if cmd == 1:
            pass
        else:
            pass
