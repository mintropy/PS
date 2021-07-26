"""
Title : 가장 큰 증가 부분 수열
Link : https://www.acmicpc.net/problem/17214
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
max_sum_sub_seq = seq[::]
max_sum_sub_seq[0] = seq[0]
max_sum = seq[0]


for i in range(1, n):
    m = seq[i]
    for j in range(i - 1, -1, -1):
        if seq[j] < m:
            tmp_sum = max_sum_sub_seq[j] + m
            # 최댓값이 아닐 때
            if tmp_sum <= max_sum_sub_seq[i]:
                continue
            # 최댓값이 되면 값 갱신
            max_sum_sub_seq[i] = tmp_sum
            if tmp_sum > max_sum:
                max_sum = tmp_sum

print(max_sum)