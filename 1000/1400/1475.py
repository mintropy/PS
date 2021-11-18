"""
Title : 방 번호
Link : https://www.acmicpc.net/problem/1475
"""

import sys
input = sys.stdin.readline


N = int(input())
nums = [0] * 9
while N:
    res = N % 10
    if res == 9:
        res = 6
    nums[res] += 1
    N //= 10

if nums[6] % 2:
    nums[6] //= 2
    nums[6] += 1
else:
    nums[6] //= 2

print(max(nums))
