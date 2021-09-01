"""
Title : 맥주 마시면서 걸어가기
Link : https://www.acmicpc.net/problem/9205
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    home = tuple(map(int, input().split()))
    conv = list(tuple(map(int, input().split())) for _ in range(n))
    festival = tuple(map(int, input().split()))
    points = [home] + conv + [festival]
    
    # 1 불가능, 0 가능
    dist = [[0] * (n + 2) for _ in range (n + 2)]
    for i in range(n + 2):
        for j in range(i + 1):
            x1, y1 = points[i]
            x2, y2 = points[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            if d > 1000:
                continue
            dist[i][j] = 1
            dist[j][i] = 1
    
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                # i에서 j까지
                dist_ij = dist[i][j]
                # i에서 j까지 k거쳐서
                dist_ik = dist[i][k]
                dist_kj = dist[k][j]
                if dist_ik and dist_kj and not dist_ij:
                    dist[i][j] = 1
    
    if dist[0][-1]:
        print('happy')
    else:
        print('sad')
