"""
Title : A를 B로
Link : https://www.acmicpc.net/problem/13019
"""

import sys
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())

if sorted(a) != sorted(b):
    print(-1)
elif a == b:
    print(0)
else:
    left_count = 0
    right_count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            left_count = i
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] != b[i]:
            right_count = i
            break
    
    print(right_count - left_count + 1)
