'''
Title : 프렉탈 평면
Link : https://www.acmicpc.net/problem/1030
'''

import sys

input = sys.stdin.readline




s, n, k, r1, r2, c2, c2 = map(int, input().split())
if n % 2:
    plane = [[0]]
elif not(n % 2):
    plane = [[0, 0], [0, 0]]

