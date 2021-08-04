"""
Title : 풍선 터트리기
Link : https://www.acmicpc.net/problem/2346
"""

import sys, collections

n = int(input())
queue = collections.deque([i for i in range(1, n + 1)])

cmd = [0] + list(map(int, input().split()))

for i in range(n):
    m = queue.popleft()
    print(m, end = ' ')
    c = cmd[m]
    if c > 0:
        queue.rotate(-1 * (c - 1))
    else:
        queue.rotate(-1 * (c))
