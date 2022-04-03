"""
Title : 좋은 구간
Link : https://www.acmicpc.net/problem/1059
"""

import sys
input = sys.stdin.readline

l = int(input())
seq = sorted((map(int, input().split())))
n = int(input())


if n in seq:
    print(0)
elif l == 1:
    left = n - 1
    right = seq[0] - n - 1

    count = 0
    # 닫힌집합의 양 끝에 n이 없는 경우
    count += left * right
    # 닫힌집합의 양 끝에 n이 있는 경우
    count += left + right
    
    print(count)
else:
    for i in range(l - 1):
        if i == 0 and n < seq[i]:
            idx = -1
            break
        if seq[i] < n < seq[i + 1]:
            idx = i
            break
    # n기준으로 바로 작은, 바로 큰 숫자
    # 그 사이에 있는 숫자들의 개수
    if idx == -1:
        left = n - 1
    else:
        left = n - seq[idx] - 1
    right = seq[idx + 1] - n - 1
    
    count = 0
    # 닫힌집합의 양 끝에 n이 없는 경우
    count += left * right
    # 닫힌집합의 양 끝에 n이 있는 경우
    count += left + right
    
    print(count)