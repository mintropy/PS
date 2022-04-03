"""
Title : 수 이어가기
Link : https://www.acmicpc.net/problem/2635
"""

import sys
input = sys.stdin.readline

n = int(input())
max_len = 0
max_len_seq = []

for i in range(n // 2, n + 1):
    tmp = [n, i]
    while True:
        t = tmp[-2] - tmp[-1]
        if t < 0:
            if len(tmp) > max_len:
                max_len = len(tmp)
                max_len_seq = tmp[::]
            break
        else:
            tmp.append(t)

print(max_len)
print(*max_len_seq)
