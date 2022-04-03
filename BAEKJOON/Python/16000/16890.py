"""
Title : 창업
Link : https://www.acmicpc.net/problem/16890
"""

import sys
input = sys.stdin.readline


ko_alp = sorted(list(input().strip()), reverse=True)
cu_alp = sorted(list(input().strip()))
l = len(ko_alp)

if l % 2:
    ko_alp = ko_alp[l//2:]
    cu_alp = cu_alp[l//2+1:]
else:
    ko_alp = ko_alp[l//2:]
    cu_alp = cu_alp[l//2:]

ans_front = ''
ans_back = ''
ko_idx = cu_idx = 0

for i in range(l):
    if i % 2:
        try:
            cu_alp[-1] >= ko_alp[-1]
            ans_front += cu_alp.pop()
        except:
            ans_back += cu_alp[0]
            cu_idx += 1
    else:
        try:
            ko_alp[-1] <= cu_alp[-1]
            ans_front += ko_alp.pop()
        except:
            ans_back += ko_alp[0]
            ko_idx += 1

ans_back = ans_back[::-1]
print(ans_front + ans_back)
