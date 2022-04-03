"""
Title : 비숍 투어
Link : 
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
sx, sy = MIIS()
ex, ey = MIIS()

if (sx + sy) % 2 == (ex + ey) % 2:
    if N == 1 or M == 1:
        if sx == ex and sy == ey:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')

'''
10 9
1 1
2 5

'''
