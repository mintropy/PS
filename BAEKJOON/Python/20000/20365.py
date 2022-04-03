"""
Title : 블로그2
Link : https://www.acmicpc.net/problem/20365
"""

n = int(input())
color = input().strip()

red = 0
blue = 0
now = color[0]

for i in range(n):
    if color[i] == now:
        continue
    else:
        if now == 'R':
            red += 1
        else:
            blue += 1
        now = color[i]
if now == 'R':
    red += 1
else:
    blue += 1
now = color[i]

if red == blue:
    print(blue + 1)
else:
    print(min(red, blue) + 1)