from sys import stdin
from typing import Counter

#n, s = map(int, stdin.readline().split())
#seq = list(map(int, stdin.readline().split()))

n, s = 5, 0
seq = [-7, -3, -2, 5, 8]

def dfs(idx, sum, l, changed = False):
    global n, s, seq, count
    if changed and sum == s and l != 0:
        count += 1
    if idx == n:
        return
    dfs(idx + 1, sum, l)
    sum += seq[idx]
    dfs(idx + 1, sum, l + 1, True)
    sum -= seq[idx]

count = 0
dfs(0, 0, 0)
print(count)



'''
itertools 활용하는 방법
'''

import itertools

n, m = map(int, input().split())
numlist = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    sub = itertools.combinations(numlist, i)
    for x in sub:
        if sum(x) == m:
            cnt += 1

print(cnt)