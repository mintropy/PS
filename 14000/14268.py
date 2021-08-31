"""
Title : 회사 문화 2
Link : https://www.acmicpc.net/problem/14268
"""

import sys
input = sys.stdin.readline


def update(i, w):
    while i != -1:
        company[i] += w
        i = sup[i]
    return


n, m = map(int ,input().split())
company = [0] * (n + 1)
sup = [0] + list(map(int, input().split()))


for _ in range(m):
    query, *todo = map(int, input().split())
    
    if query == 1:
        update(*todo)
    else:
        print(company[todo[0]])
