"""
Title : 횡단보도
Link : https://www.acmicpc.net/problem/24042
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
green_lights = [tuple(MIIS()) for _ in range(M)]

times = [10 ** 9] * (N + 1)
times[1] = 0

cycle = 0
while True:
    for i in range(M):
        s, e = green_lights[i]
        if times[s] == 10 ** 9 and times[e] == 10 ** 9:
            continue
        if times[s] != 10 ** 9 and times[e] != 10 ** 9:
            continue
        if times[s] == 10 ** 9:
            s, e = e, s
        times[e] = cycle * M + i + 1
        if e == N:
            print(times[e])
            exit()
    cycle += 1
