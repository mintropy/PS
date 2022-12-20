"""
Title : 수열과 쿼리 37
Link : https://www.acmicpc.net/problem/18436
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, seq: list[int]) -> None:
        self.seq = seq
        self.seq_idx = [0] * (len(seq) + 1)
        self.segment_tree = [[0, 0] for _ in range(1 << ceil(log2(len(seq))) + 1)]
        self.init_tree(1, 0, len(seq) - 1)

    def init_tree(self, node: int, st: int, end: int) -> None:
        if st == end:
            self.segment_tree[node][self.seq[st] % 2] += 1
            self.seq_idx[st + 1] = node
            return
        mid = (st + end) // 2
        self.init_tree(node * 2, st, mid)
        self.init_tree(node * 2 + 1, mid + 1, end)
        self.segment_tree[node] = [
            self.segment_tree[node * 2][0] + self.segment_tree[node * 2 + 1][0],
            self.segment_tree[node * 2][1] + self.segment_tree[node * 2 + 1][1],
        ]

    def update_tree(self, node: int, value: int) -> None:
        idx = self.seq_idx[node]
        self.segment_tree[idx] = [0, 0]
        self.segment_tree[idx][value % 2] += 1
        while idx >= 2:
            idx //= 2
            self.segment_tree[idx] = [
                self.segment_tree[idx * 2][0] + self.segment_tree[idx * 2 + 1][0],
                self.segment_tree[idx * 2][1] + self.segment_tree[idx * 2 + 1][1],
            ]

    def query(
        self, node: int, st: int, end: int, left: int, right: int, even: int
    ) -> int:
        if end < left or right < st:
            return 0
        elif left <= st and end <= right:
            return self.segment_tree[node][even]
        mid = (st + end) // 2
        l_count = self.query(node * 2, st, mid, left, right, even)
        r_count = self.query(node * 2 + 1, mid + 1, end, left, right, even)
        return l_count + r_count


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree(seq)
    M = II()
    for _ in range(M):
        cmd, x, y = MIIS()
        match cmd:
            case 1:
                segment_tree.update_tree(x, y)
            case 2:
                print(segment_tree.query(1, 1, N, x, y, 0))
            case 3:
                print(segment_tree.query(1, 1, N, x, y, 1))
