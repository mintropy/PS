"""
Title : 스카이라인
Link : https://www.acmicpc.net/problem/1933
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
buildings = [tuple(map(int, input().split())) for _ in range(n)]

heap = []
now = 0
for st, height, end in buildings:
    # 지금 높이 0일 때
    if not heap:
        print(st, height, end=' ')
        heapq.heappush(heap, (end, height))
        now = height
    # 건물이 있을 때
    else:
        # 새로운 건물 이전에 끝나는 건물이 있을 때
        while heap and st <= heap[0][0]:
            e, h = heapq.heappop(heap)
            if e == st:
                continue
            if now != h:
                print(e, h, end=' ')
                now = h
        if not heap:
            print(e, 0)
            now = 0
        if height > now:
            print(st, height, end=' ')
            now = height
        heapq.heappush(heap, (end, height))

