"""
Title : 예쁜 케이크
Link : https://www.acmicpc.net/problem/24040
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    if (N + 1) % 3 == 0:
        print('TAK')
    elif N % 3 == 0 and (N // 3) % 3 == 0:
        print('TAK')
    else:
        print('NIE')
