"""
Title : 후위 표기식
Link : https://www.acmicpc.net/problem/1918
"""

poly = list(input().strip())

ans = ''
stack = []
for i in range(len(poly)):
    if poly[i] == '(':
        stack.append(poly[i])
    elif poly[i].isalpha():
        ans += poly[i]
    elif poly[i] in '+-':
        if not stack:
            stack.append(poly[i])
        else:
            while True:
                if not stack:
                    stack.append(poly[i])
                    break
                elif stack[-1] in '*/+-':
                    ans += stack.pop()
                else:
                    stack.append(poly[i])
                    break
    elif poly[i] in '*/':
        if not stack or stack[-1] == '(+-':
            stack.append(poly[i])
        else:
            while True:
                if not stack:
                    stack.append(poly[i])
                    break
                elif stack[-1] in '*/':
                    ans += stack.pop()
                else:
                    stack.append(poly[i])
                    break
    elif poly[i] == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            else:
                ans += stack.pop()

# 남은 연산자가 있을 때
while stack:
    ans += stack.pop()

print(ans)
