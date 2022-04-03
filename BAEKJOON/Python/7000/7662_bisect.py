"""
Title : 이중 우선순위 큐
Link : https://www.acmicpc.net/problem/7662
"""

import sys, bisect, collections
input = sys.stdin.readline


for _ in range(int(input())):
    heap = collections.deque([])
    for _ in range(int(input())):
        cmd = list(map(str, input().strip().split()))
        if cmd[0] == 'I':
            n = int(cmd[1])
            if not heap:
                heap.append(n)
            else:
                bisect.insort_left(heap, n)
        else:
            if not heap:
                continue
            if cmd[1] == '1':
                heap.pop()
            else:
                heap.popleft()
    
    if heap:
        print(heap[-1], heap[0])
    else:
        print('EMPTY')
