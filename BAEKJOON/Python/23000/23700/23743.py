"""
Title : 방탈출
Link : https://www.acmicpc.net/problem/23743
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    rooms = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = MIIS()
        rooms[a].append((b, c))
    
