"""
Title : 숫자 고르기
Link : https://www.acmicpc.net/problem/2230
"""

import sys, heapq, collections
input = sys.stdin.readline

n, m = map(int, input().split())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

min_diff = 3 * 10 ** 9
num = collections.deque([])

while heap:
    right = heapq.heappop(heap)
    num.append(right)
    while num:
        left = num[0]
        diff = right - left
        if diff >= m:
            if diff < min_diff:
                min_diff = diff
            num.popleft()
        else:
            break


print(min_diff)
