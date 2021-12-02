"""
Title : 창업
Link : https://www.acmicpc.net/problem/16890
"""

import sys
input = sys.stdin.readline


ko_alp = sorted(list(input().strip()), reverse=True)
cu_alp = sorted(list(input().strip()))

ans = ''

for i in range(len(ko_alp)):
    if i % 2:
        ans += cu_alp.pop()
    else:
        ans += ko_alp.pop()

print(ans)
