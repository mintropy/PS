"""
Title : 괄호의 값
Link : https://www.acmicpc.net/problem/2504
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    brackets = input().strip()
    pair = {")": "(", "]": "["}
    stack = []
    points = 0
    for x in brackets:
        if x == "(" or x == "[":
            stack.append(x)
        else:
            tmp = 0
            while stack:
                if isinstance(stack[-1], int):
                    tmp += stack.pop()
                else:
                    break
            if not stack or stack[-1] != pair[x]:
                stack.append(x)
                break
            if not tmp:
                tmp = 1
            if x == ")":
                tmp *= 2
            elif x == "]":
                tmp *= 3
            stack.pop()
            if not stack:
                points += tmp
            else:
                stack.append(tmp)
    if stack:
        print(0)
    else:
        print(points)
