"""
Title : 합
Link : https://www.acmicpc.net/problem/1132
"""

import sys
input = sys.stdin.readline


n = int(input())

alp_count = {chr(i): [0] * 12 for i in range(65, 76)}

for _ in range(n):
    num = 'K' * 12 + input().strip()
    num = num[::-1]
    for i in range(12):
        alp_count[num[i]][i] += 1

alp_count_list = sorted(alp_count.items(), key=lambda x: x[1])


print()

