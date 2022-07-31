"""
Title : 큐 2
Link : https://www.acmicpc.net/problem/18258
"""

import sys, collections
input = sys.stdin.readline

n = int(input())
queue = collections.deque([])

for _ in range(n):
    # cmd = list(map(str, input().strip().split()))
    cmd, *m = map(str, input().strip().split())

    if cmd == 'push':
        queue.append(int(m[0]))
    elif cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])