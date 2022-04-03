"""
Title : iSharp
Link : https://www.acmicpc.net/problem/3568
"""

import sys
vars = list(input().strip().split())

basic_type = vars[0]

for var in vars[1:]:
    tmp = basic_type
    var_name = ''
    for i in range(len(var)):
        if not var[i].isalpha():
            break
    for j in range(len(var) - 2, i - 1, -1):
        if var[j] == ']':
            tmp += '[]'
        elif var[j] == '[':
            continue
        else:
            tmp += var[j]
    tmp += ' ' + var[:i] + ';'
    print(tmp)
