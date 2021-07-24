"""
Title : 수 정렬하기 3
Link : https://www.acmicpc.net/problem/10989
"""

import sys, collections

input = sys.stdin.readline

num_count = collections.defaultdict(int)
for _ in range(int(input())):
    num_count[int(input())] += 1

for key in sorted(num_count.keys()):
    for _ in range(num_count[key]):
        print(key)