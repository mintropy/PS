'''
Title : 수 정렬하기
Link : https://www.acmicpc.net/problem/2750
'''

import sys

input = sys.stdin.readline

n = int(input())
numbers = list(int(input()) for _ in range(n))

for i in range(n):
    min_idx = i
    minimum = numbers[i]
    for j in range(i, n):
        if numbers[j] < minimum:
            min_idx = j
            minimum = numbers[j]
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

for num in numbers:
    print(num)