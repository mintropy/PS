"""
Title : 사다리 게임
Link : https://www.acmicpc.net/problem/2008
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, x, y = map(int, input().split())
horizontal_line = list(int(input()) for _ in range(m))

