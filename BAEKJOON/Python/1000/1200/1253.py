"""
Title : 좋다
Link : https://www.acmicpc.net/problem/1253
"""

import sys
input = sys.stdin.readline


N = int(input())
# seq = sorted(map(int, input().split()))
seq = list(map(int, input().split()))
seq.sort()

count = 0

for i in range(N):
    target = seq[i]
    left, right = 0, N - 2
    tmp_seq = seq[:i] + seq[i+1:]
    while left < right:
        now = tmp_seq[left] + tmp_seq[right]
        if now == target:
            count += 1
            break
        elif now > target:
            right -= 1
        elif now < target:
            left += 1

print(count)


'''
N = int(input())
seq = sorted(map(int, input().split()))

count = 0

for i in range(N):
    left, right = 0, N - 1
    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        elif seq[left] + seq[right] == seq[i]:
            count += 1
            break
        elif seq[left] + seq[right] > seq[i]:
            right -= 1
        elif seq[left] + seq[right] < seq[i]:
            left += 1

print(count)
'''
