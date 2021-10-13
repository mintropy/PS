"""
Title : 자동차경주 
Link : https://www.acmicpc.net/problem/2611
"""

import collections
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
roads = [[] for _ in range(n)]
for _ in range(m):
    p, q, r = map(int, input().split())
    roads[p].append[(q, r)]

# i도시 j번재에 도착했을 때, 이전 도시
dp = [[0] * n for _ in range(n)]

queue = collections.deque([1])
while queue:
    x = queue.popleft()
    score_noew = dp[x][0]
    for y, score in roads[x]:
        pass



