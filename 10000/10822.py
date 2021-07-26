"""
Title : 더하기
Link : https://www.acmicpc.net/problem/10822
"""

import sys

input = sys.stdin.readline

print(sum(list(int(i) for i in input().strip().split(','))))