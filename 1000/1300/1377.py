"""
Title : 버블 소트
Link : https://www.acmicpc.net/problem/1377
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = [list(map(int, input().split())) for _ in range(n)]


def bubble_sort(n, seq):
    for i in range(n):
        change = False
        for j in range(i, n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                change = True
        if not change:
            return i + 1

print(bubble_sort(n, seq))
