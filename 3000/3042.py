"""
Title : 트리플렛
Link : https://www.acmicpc.net/problem/3042
"""

import sys
input = sys.stdin.readline

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
check = [[False] * n for _ in range(n)]

count = 0

