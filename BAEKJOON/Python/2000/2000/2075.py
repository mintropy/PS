"""
Title : N번째 큰 수
Link : https://www.acmicpc.net/problem/2075
"""

import sys, heapq
input = sys.stdin.readline

n = int(input())

heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(1, n):
    tmp = list(map(int , input().split()))
    for x in tmp:
        heapq.heappushpop(heap, x)

print(heap[0])
