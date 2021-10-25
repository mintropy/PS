"""
Title : 동작 그만. 밑장 빼기냐?
Link : https://www.acmicpc.net/problem/20159
"""

import sys
input = sys.stdin.readline


n = int(input())
cards = list(map(int, input().split()))

prefix_sum = [cards[-2]]

for i in range(n - 4, -1, -2):
    prefix_sum.append(prefix_sum[-1] + cards[i])

prefix_sum = [prefix_sum[-1]] + prefix_sum[::-1] + [0]
max_sum = prefix_sum[0]

# 홀수번째 차례에 및장 빼기
for i in range(n // 2):
    if max_sum < (prefix_sum[0] - prefix_sum[i + 1]) + cards[i * 2 + 1] + prefix_sum[i + 2]:
        max_sum = (prefix_sum[0] - prefix_sum[i + 1]) + cards[i * 2 + 1] + prefix_sum[i + 2]
# 짝수번째 차례에 및장 빼기
for i in range(1, n // 2):
    if max_sum < (prefix_sum[0] - prefix_sum[i + 1]) + cards[i * 2 - 1] + prefix_sum[i + 2]:
        max_sum = (prefix_sum[0] - prefix_sum[i + 1]) + cards[i * 2 - 1] + prefix_sum[i + 2]

print(max_sum)

'''
Conter Example
8
2 1 1 1 2 2 1 1
ans : 7
out : 6
'''
