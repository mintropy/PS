"""
Title : 스티커 정리 1
Link : https://www.acmicpc.net/problem/1101
"""

import sys, collections
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()

box = [list(MIIS()) for _ in range(N)]
