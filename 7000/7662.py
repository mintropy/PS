"""
Title : 이중 우선순위 큐
Link : https://www.acmicpc.net/problem/7662
"""

import sys, collections
input= sys.stdin.readline


for _ in range(int(input())):
    heap = collections.deque([])
    for i in range(int(input())):
        cmd, n = map(str, input().strip().split())
        n = int(n)
        if cmd == 'I':
            if not heap:
                heap.append(n)
            else:
                cnt = 0
                for j in range(len(heap)):
                    if n <= heap[0]:
                        break
                    else:
                        heap.rotate(-1)
                        cnt += 1
                heap.appendleft(n)
                heap.rotate(cnt)
        else:
            if len(heap) == 0:
                continue
            elif n == 1:
                heap.pop()
            else:
                heap.popleft()
    if heap:
        print(heap[-1], heap[0])
    else:
        print('EMPTY')


'''
# heap 시간초과
import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    heap = []
    # 명령 수행
    for i in range(int(input())):
        cmd, n = map(str, input().strip().split())
        if cmd == 'I':
            heapq.heappush(heap, int(n))
        else:
            if len(heap) == 0:
                continue
            if n == '-1':
                heapq.heappop(heap)
            else:
                heap = heapq.nsmallest(len(heap) - 1, heap)
                heapq.heapify(heap)
    # 출력
    if heap:
        print(heapq.nlargest(1, heap)[0], heap[0])
    else:
        print('EMPTY')
'''