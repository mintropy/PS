"""
Title : 가장 긴 증가하는 부분 수열 5
Link : https://www.acmicpc.net/problem/14003
"""

import sys, bisect
input = sys.stdin.readline


n = int(input())
seq = list(map(int, input().split()))


# lower_bound를 탐색, 저장하는 리스트
lower_bound = [seq[0]]
# lower_bound에 나타나는 인덱스를 저장하는 리스트
lower_bound_idx = [0] * n


for i in range(1, n):
    s = seq[i]
    idx = bisect.bisect_left(lower_bound, s)
    if idx == len(lower_bound):
        lower_bound.append(s)
    else:
        lower_bound[idx] = s
    lower_bound_idx[i] = idx


min_sub_seq = []
idx = len(lower_bound) - 1

for i in range(n - 1, -1, -1):
    if idx == -1:
        break
    if lower_bound_idx[i] == idx:
        min_sub_seq.append(seq[i])
        idx -= 1

print(len(min_sub_seq))
min_sub_seq.reverse()
print(*min_sub_seq)