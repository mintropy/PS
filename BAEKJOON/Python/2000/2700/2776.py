"""
Title : 암기왕
Link : https://www.acmicpc.net/problem/2776
"""

import sys
input = sys.stdin.readline


def bin_search(st, end, k, note1):
    while st <= end:
        mid = (st + end) // 2
        n1 = note1[mid]
        if n1 == k:
            return 1
        elif n1 > k:
            end = mid - 1
        else:
            st = mid + 1
    return 0


for _ in range(int(input())):
    n = int(input())
    note1 = sorted(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    for n2 in note2:
        print(bin_search(0, n - 1, n2, note1))