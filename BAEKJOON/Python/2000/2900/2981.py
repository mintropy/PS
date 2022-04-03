"""
Title : 검문
Link : https://www.acmicpc.net/problem/2981
"""

import sys
input = sys.stdin.readline


def find_gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
seq = list(int(input()) for _ in range(n))

gcd = find_gcd(seq[0], seq[1])
for i in range(2, n):
    gcd = find_gcd(seq[i], gcd)

for i in range(2, gcd + 1):
    if not (gcd % i):
        print(i, end='')
