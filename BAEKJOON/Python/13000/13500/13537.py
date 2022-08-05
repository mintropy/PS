"""
Title : 수열과 쿼리 1
Link : https://www.acmicpc.net/problem/13537
"""

import sys, bisect
input = sys.stdin.readline


class MergeSortTree():
    def __init__(self, seq):
        self.seq = seq
        self.merge_sort_tree = [[seq]]
    
    def make_merge_sort_tree(self):
        # sort되지 않은 상태로 먼저 구간 분할
        while True:
            if len(self.merge_sort_tree[-1]) == len(self.seq):
                break
            tmp = []
            for sub_seq in self.merge_sort_tree[-1]:
                l = len(sub_seq) // 2
                if l != 0:
                    tmp.append(sub_seq[:l])
                tmp.append(sub_seq[l:])
            self.merge_sort_tree.append(tmp)
        # 모든 sub_seq 정렬
        for i in range(len(self.merge_sort_tree)):
            for j in range(len(self.merge_sort_tree[i])):
                self.merge_sort_tree[i][j].sort()
    
    def count(self, st, end, i, j, k):
        # [i, j]구간에서 k이상의 수의 개수
        # 지금 바라보는 전체 구간 [st, end]
        if j < st or i > end:
            return 0
        
        pass


n = int(input())
seq = list(map(int, input().split()))

merge_sort_tree = MergeSortTree(seq)
merge_sort_tree.make_merge_sort_tree()
print()