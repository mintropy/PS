"""
Title : 램프
Link : https://www.acmicpc.net/problem/1034
"""

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lamps = [tuple(int(i) for i in input().strip()) for _ in range(N)]
K = int(input())

same_state = {}
for lamps_line in lamps:
    if lamps_line in same_state:
        same_state[lamps_line] += 1
    else:
        same_state[lamps_line] = 1

states = sorted(same_state.items(), key=lambda x: -x[1])
for i in range(len(states)):
    state, count = states[i]
    zero_count = state.count(0)
    if zero_count <= K and (K - zero_count) % 2 == 0:
        print(count)
        break
else:
    print(0)
