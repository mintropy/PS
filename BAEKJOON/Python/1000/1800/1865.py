"""
Title : 웜홀
Link : https://www.acmicpc.net/problem/1865
"""

import sys
input = sys.stdin.readline


def bellman_ford():
    global n, m, w
    global roads, wormhole
    points = [0] * (n + 1)
    # 웜홀 처리 >> 도로 처리
    for _ in range(n - 1):
        update = False
        for s in range(1, n + 1):
            for e, t in move[s]:
                if points[s] + t < points[e]:
                    points[e] = points[s] + t
                    update = True
        if not update:
            break
    # 음수 사이클 확인
    for s in range(1, n + 1):
        for e, t in move[s]:
            if points[s] + t < points[e]:
                return True
    return False


for tc in range(int(input())):
    n, m, w = map(int, input().split())
    
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    wormhole = [tuple(map(int, input().split())) for _ in range(w)]
    move = [[] for _ in range(n + 1)]
    for s, e, t in roads:
        move[s].append((e, t))
        move[e].append((s, t))
    for s, e, t in wormhole:
        move[s].append((e, -t))
    
    if bellman_ford():
        print('YES')
    else:
        print('NO')
