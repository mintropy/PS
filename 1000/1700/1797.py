"""
Title : 균형잡힌 줄서기
Link : https://www.acmicpc.net/problem/1797
"""

import sys
input = sys.stdin.readline


N = int(input())
members = [tuple(map(int, input().split())) for _ in range(N)]
members.sort(key=lambda x:x[1])






# print(max_continuous)
