"""
Title : 균형잡힌 세상
Link : https://www.acmicpc.net/problem/4949
"""

import sys
input = sys.stdin.readline

while True:
    ip = str(input().rstrip())
    if ip == '.':
        break
    world = list(ip)
    
    stack = []
    for w in world:
        if w not in ['(', ')', '[', ']']:
            continue
        if stack == []:
            stack.append(w)
        elif w == ']' and stack[-1] == '[':
            stack.pop()
        elif w == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(w)
    
    if stack == []:
        print('yes')
    else:
        print('no')