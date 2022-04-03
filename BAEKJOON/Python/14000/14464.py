"""
Title : 소가 길을 건너는 이유 4
Link : https://www.acmicpc.net/problem/14464
"""

import sys, heapq

input = sys.stdin.readline


c, n = map(int, input().split())
chickens = []
# 소가 지날수 있는 시작, 끝 시간을 기준으로 정렬한 heap
cows_start = []
cows_end = []

for _ in range(c):
    heapq.heappush(chickens, int(input()))

for i in range(n):
    s, e =map(int, input().split())
    heapq.heappush(cows_start, (s, e, i))
    heapq.heappush(cows_end, (e, s, i))

cow_crossed = [False] * n
cow_count = 0

s1, e1, c1 = heapq.heappop(cows_start)
e2, s2, c2 = heapq.heappop(cows_start)
ch = heapq.heappop(chickens)



print(cow_count)