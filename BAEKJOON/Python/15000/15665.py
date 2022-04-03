"""
Title : 별 찍기 - 11
Link : https://www.acmicpc.net/problem/15665
"""

import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(set(seq))

if m == 1:
    for num in seq:
        print(num)
else:
    ans = list(itertools.product(seq, repeat = m))
    for nums in ans:
        for num in nums:
            print(num, end = ' ')
        print()