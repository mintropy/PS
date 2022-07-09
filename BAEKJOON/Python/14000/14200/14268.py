"""
Title : 회사 문화 2
Link : https://www.acmicpc.net/problem/14268
"""

import sys
input = sys.stdin.readline


def update(i, w):
    check = [i]
    idx = 0
    while idx < len(check):
        j = check[idx]
        company[j] += w
        check += junior[j]
        idx += 1


n, m = map(int ,input().split())
company = [0] * (n + 1)
# 각 사원의 상사
sup = [0] + list(map(int, input().split()))
# 각 사원의 부하
junior = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    junior[sup[i]].append(i)


for _ in range(m):
    query, *todo = map(int, input().split())
    if query == 1:
        update(*todo)
    else:
        print(company[todo[0]])
