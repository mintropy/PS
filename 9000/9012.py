"""
Title : 괄호
Link : https://www.acmicpc.net/problem/9012
"""

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    ps = list(str(input().strip()))
    check = []
    for p in ps:
        if check == []:
            check.append(p)
        elif check[-1] == '(' and p == ')':
            check.pop()
        else:
            check.append(p)
    if check == []:
        print('YES')
    else:
        print('NO')