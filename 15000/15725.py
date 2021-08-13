"""
Title : 다항함수의 미분
Link : https://www.acmicpc.net/problem/15725
"""

poly = str(input())

idx = 0
while idx < len(poly):
    if poly[idx] == 'x':
        break
    idx += 1

if idx == 0:
    print(1)
elif idx == len(poly):
    print(0)
else:
    try:
        int(poly[idx - 1])
        print(poly[:idx])
    except:
        print(-1)
