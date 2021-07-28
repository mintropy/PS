"""
Title : 결혼식
Link : https://www.acmicpc.net/problem/5567
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

merrige = [False for _ in range(n + 1)]
merrige[1] = True

for friend in friends[1]:
    merrige[friend] = True
    for f in friends[friend]:
        merrige[f] = True

count = 0
for tf in merrige:
    if tf:
        count += 1

print(count - 1)