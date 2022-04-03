'''
Title : 숫자의 신
Link : https://www.acmicpc.net/problem/1422
'''

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
ints = sorted([int(input()) for _ in range(k)])

