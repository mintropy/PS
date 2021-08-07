"""
Title : 알고리즘 기말고자
Link : https://www.acmicpc.net/problem/10424
"""

import sys
input = sys.stdin.readline

n = int(input())
grade = list(map(int, input().split()))

satisfaction = []

for i in range(n):
    g = grade[i]
    # B
    b = 0
    for j in range(0, i):
        if grade[j] > g:
            b += 1
    # C
    c = 0
    for j in range(i + 1, n):
        if grade[j] < g:
            c += 1
    
    # A = B - C
    satisfaction.append(b - c)

print(*satisfaction, sep = '\n')