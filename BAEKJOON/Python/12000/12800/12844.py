"""
Title : XOR
Link : https://www.acmicpc.net/problem/12844
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
        self.tree = [0] * (1 << (ceil(log2(N)) + 1))
        self.lazy = [0] * len(self.tree)
        self.seq_to_tree = [0] * (N + 1)
        self.make_link_list(1, 1, N)
        self.init_tree()

    def make_link_list(self, node: int, start: int, end: int) -> None:
        if start >= end:
            self.seq_to_tree[start] = node
            return
        mid = (start + end) // 2
        self.make_link_list(node * 2, start, mid)
        self.make_link_list(node * 2 + 1, mid + 1, end)

    def init_tree(self) -> None:
        l = len(self.tree)
        for idx, x in enumerate(self.seq_to_tree):
            self.tree[x] = self.seq[idx]
        for i in range(l - 1, 0, -1):
            if i * 2 + 1 >= l or self.tree[i]:
                continue
            self.tree[i] = self.tree[i * 2] ^ self.tree[i * 2 + 1]

    def update(self, left: int, right: int, k: int) -> None:
        for i in range(left, right + 1):
            self.seq[i] ^= k
        self.update_tree(1, 1, N, left, right, k)

    def update_tree(
        self, node: int, start: int, end: int, left: int, right: int, k: int
    ) -> None:
        if right < start or end < left:
            return
        if start == end:
            self.tree[node] ^= k ^ self.lazy[node]
            self.lzay[node] = 0
            return
        if self.lazy[node]:
            _lazy = self.lazy[node]
            self.tree[node] ^= _lazy
            self.lazy[node * 2] ^= _lazy
            self.lazy[node * 2 + 1] ^= _lazy
            self.lazy[node] = 0
        if start <= right and left <= end:
            self.tree[node] ^= k
            self.lazy[node * 2] ^= k
            self.lazy[node * 2 + 1] ^= k
            return
        mid = (start + end) // 2
        self.update_tree(node * 2, start, mid, left, right)
        self.update_tree(node * 2 + 1, mid + 1, end, left, right)
        self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def get_xor(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if start == end:
            self.tree[node] ^= self.lazy[node]
            self.lazy[node] = 0
            return self.tree[node]
        if self.lazy[node]:
            _lazy = self.lazy[node]
            self.tree[node] ^= _lazy
            self.lazy[node * 2] ^= _lazy
            self.lazy[node * 2 + 1] ^= _lazy
            self.lazy[node] = 0
        if start <= right and left <= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_xor = self.get_xor(node * 2, start, mid, left, right)
        right_xor = self.get_xor(node * 2 + 1, mid + 1, end, left, right)
        return left_xor ^ right_xor


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree(N, seq)
    for _ in range(II()):
        cmd, *query = MIIS()
        if cmd == 1:
            i, j, k = query
            segment_tree.update(i + 1, j + 1, k)
        else:
            i, j = query
            print(segment_tree.get_xor(1, 1, N, i + 1, j + 1))
