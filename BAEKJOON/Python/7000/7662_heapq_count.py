"""
Title : 이중 우선순위 큐
Link : https://www.acmicpc.net/problem/7662
"""

import sys
import heapq
input = sys.stdin.readline


for _ in range(int(input())):
    min_heap = []
    max_heap = []
    
    k = int(input())
    visited = [False] * (k)
    for i in range(k):
        cmd, num = input().strip().split()
        if cmd == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            visited[i] = True
        elif num == '1':
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        elif num == '-1':
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
    
    result = []
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
