"""
Title : 스택수열
Link : https://www.acmicpc.net/problem/1874
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = list(int(input()) for _ in range(n))

idx = 0
stack = []
result = []
for i in range(1, n + 1):
    stack.append(i)
    result.append('+')
    while True:
        if idx == n:
            break
        if stack == []:
            break
        if stack[-1] != seq[idx]:
            break
        stack.pop()
        result.append('-')
        idx += 1

if stack:
    print('NO')
else:
    for cmd in result:
        print(cmd)