"""
Title : 동작 그만. 밑장 빼기냐?
Link : https://www.acmicpc.net/problem/20159
"""

import sys
input = sys.stdin.readline


n = int(input())
cards = list(map(int, input().split()))

prefix_sum_first = [cards[-2]]
prefix_sum_second = [cards[-1]]

for i in range(n - 3, -1, -1):
    if i % 2:
        prefix_sum_second.append(prefix_sum_second[-1] + cards[i])
    else:
        prefix_sum_first.append(prefix_sum_first[-1] + cards[i])

prefix_sum_first.reverse()
prefix_sum_second.reverse()

max_sum = prefix_sum_first[0]

# 홀수번째 차례에 및장빼기
# 처음 마지막은 따로 처리
if max_sum < cards[1] + prefix_sum_first[1]:
    max_sum = cards[1] + prefix_sum_first[1]
if n >= 4 and max_sum < cards[n - 1] + prefix_sum_first[0] - prefix_sum_first[-1]:
    max_sum = cards[n - 1] + prefix_sum_first[0] - prefix_sum_first[-1]
for i in range(1, n // 2 - 1):
    if max_sum < (prefix_sum_first[0] - prefix_sum_first[i]) + cards[i * 2 + 1] + prefix_sum_first[i + 1]:
        max_sum = (prefix_sum_first[0] - prefix_sum_first[i]) + cards[i * 2 + 1] + prefix_sum_first[i + 1]
# 짝수번째 차례에 및장빼기
# 처음 마지막은 따로 처리
if n == 4 and max_sum < cards[0] + cards[3]:
    max_sum = cards[0] + cards[1]
elif n > 4 and max_sum < cards[0] + cards[3] + prefix_sum_first[2]:
    max_sum = cards[0] + cards[1] + prefix_sum_first[2]
if n > 4 and max_sum < (prefix_sum_first[0] - prefix_sum_first[-1]) + cards[-3]:
    max_sum = (prefix_sum_first[0] - prefix_sum_first[-1]) + cards[-3]
for i in range(1, n // 2 - 2):
    if max_sum < (prefix_sum_first[0] - prefix_sum_first[i + 1]) + cards[i * 2] + prefix_sum_first[i + 2]:
        max_sum < (prefix_sum_first[0] - prefix_sum_first[i + 1]) + cards[i * 2] + prefix_sum_first[i + 2]

print(max_sum)

'''
Conter Example
8
2 1 1 1 2 2 1 1
ans : 7
out : 6
'''
