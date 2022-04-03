"""
Title : 에라토스테네스의 체
Link : https://www.acmicpc.net/problem/2960
"""

n, k = map(int, input().split())

num = [True] * (n + 1)
deleted = 0
for i in range(2, n + 1):
    if num[i]:
        for j in range(i, n + 1, i):
            if num[j]:
                num[j] = False
                deleted += 1
                if deleted == k:
                    print(j)
