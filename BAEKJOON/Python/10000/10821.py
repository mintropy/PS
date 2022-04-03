"""
Title : 정수의 개수
Link : https://www.acmicpc.net/problem/10821
"""

import sys

input = sys.stdin.readline

print(len(list(int(i) for i in input().strip().split(','))))