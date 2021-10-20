"""
Title : 가희와 읽기 쓰기 놀이
Link : https://www.acmicpc.net/problem/21776
"""

import sys
input = sys.stdin.readline


c, n = map(int, input().split())
turn = [tuple(map(int, input().split())) for _ in range(n)]

