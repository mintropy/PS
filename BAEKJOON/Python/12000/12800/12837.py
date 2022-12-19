"""
Title : 가계부 (Hard)
Link : https://www.acmicpc.net/problem/12837
"""

from math import log2, ceil
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, Q: int) -> None:
        self.segment_tree = [[0] * 3 for _ in range(1 << ceil(log2(Q)) + 1)]
        self.leaf_idx = len(self.segment_tree) // 2

    def update_tree(self, day, money) -> None:
        idx = self.leaf_idx
        self.segment_tree[idx] = [day, day, money]
        while idx >= 2:
            if idx % 2:
                self.segment_tree[idx // 2][2] += self.segment_tree[idx][2]
            else:
                self.segment_tree[idx // 2][2] = self.segment_tree[idx][2]
            self.segment_tree[idx // 2][0] = self.segment_tree[idx][0]
            self.segment_tree[idx // 2][1] = self.segment_tree[idx][1]
            idx //= 2
        self.leaf_idx += 1

    def query(self, node: int, left: int, right: int) -> int:
        st, end, m = self.segment_tree[node]
        if st == 0 == end:
            return 0
        if left > end or st < right:
            return 0
        if left <= st and end <= right:
            return m
        lsum = self.query(node * 2, left, right)
        rsum = self.query(node * 2 + 1, left, right)
        return lsum + rsum


if __name__ == "__main__":
    N, Q = MIIS()
    segment_tree = SegmentTree(Q)
    for _ in range(Q):
        t, x, y = MIIS()
        if t == 1:
            segment_tree.update_tree(x, y)
        else:
            print(segment_tree.query(1, x, y))
