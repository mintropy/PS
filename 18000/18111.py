"""
Title : 랜선 자르기
Link : https://www.acmicpc.net/problem/1654
"""

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
field =[list(map(int, input().split())) for _ in range(n)]
field_sotred = []
for f in field:
    field_sotred.extend(f)
field_sotred.sort(reverse = True)

count = 2 * n * m * 256 + 1
lvl = 0

for level in range(field_sotred[-1], field_sotred[0] + 1):
    block_used = 0
    move = 0
    for l in field_sotred:
        if l > level:
            block_used += l - level
            move += (l - level) * 2
        elif l == level:
            continue
        else:
            block_used -= level - l
            move += level - l
    if block_used + b < 0:
        continue
    else:
        if move <= count:
            count = move
            lvl = level

print(count, lvl)