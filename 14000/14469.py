"""
Title : 소가 길을 건너간 이유 3
Link : https://www.acmicpc.net/problem/14469
"""

import sys, heapq
input = sys.stdin.readline

n = int(input())
cows = []
for _ in range(n):
    heapq.heappush(cows, tuple(map(int, input().split())))

now = 0
for _ in range(n):
    start, duration = heapq.heappop(cows)
    if now < start:
        now = start + duration
        time = now
    else:
        now += duration

print(now)