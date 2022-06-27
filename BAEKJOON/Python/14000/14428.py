"""
Title : 수열과 쿼리 16
Link : https://www.acmicpc.net/problem/14428
"""

from math import log2
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int, seq: list) -> None:
        self.N = N
        self.seq = [0] + seq
        self.tree = [0] * (1 << (int(log2(N)) + 2))
        self.idx = [0] * (N + 1)
        self.init()

    def init(self) -> None:
        self.find_idx(1, 1, self.N)
        for idx, x in enumerate(self.idx):
            self.tree[x] = idx
        self.init_tree()

    def find_idx(self, node: int, left: int, right: int) -> None:
        if left >= right:
            self.idx[left] = node
            return
        mid = (left + right) // 2
        self.find_idx(node * 2, left, mid)
        self.find_idx(node * 2 + 1, mid + 1, right)

    def init_tree(self) -> None:
        for i in range(len(self.tree) - 1, 0, -1):
            if i * 2 + 1 > len(self.tree):
                continue
            left = self.seq[self.tree[i * 2]]
            right = self.seq[self.tree[i * 2 + 1]]
            if not left * right:
                continue
            if left <= right:
                self.tree[i] = self.tree[i * 2]
            else:
                self.tree[i] = self.tree[i * 2 + 1]

    def find(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_idx = self.find(node * 2, start, mid, left, right)
        right_idx = self.find(node * 2 + 1, mid + 1, end, left, right)
        if left_idx == 0:
            return right_idx
        if right_idx == 0:
            return left_idx
        if self.seq[left_idx] <= self.seq[right_idx]:
            return left_idx
        return right_idx

    def update(self, node: int, value: int):
        self.seq[node] = value
        tree_node = self.idx[node] // 2
        while tree_node:
            left = self.seq[self.tree[tree_node * 2]]
            right = self.seq[self.tree[tree_node * 2 + 1]]
            if left <= right:
                self.tree[tree_node] = self.tree[tree_node * 2]
            else:
                self.tree[tree_node] = self.tree[tree_node * 2 + 1]
            tree_node //= 2


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree(N, seq)
    for _ in range(II()):
        cmd, x, y = MIIS()
        if cmd == 1:
            segment_tree.update(x, y)
        else:
            print(segment_tree.find(1, 1, N, x, y))
