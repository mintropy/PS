"""
Title : IQ Test
Link : https://www.acmicpc.net/problem/1111
"""

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))


if N <= 2:
    print('A')
elif N >= 3:
    a = (seq[1] - seq[2]) // (seq[0] - seq[1])
    b = seq[2] - a * seq[0]
    possible = True
    for i in range(1, N - 1):
        if seq[i] * a + b != seq[i + 1]:
            possible = False
            break
    if possible:
        print(seq[-1] * a + b)
    else:
        print('B')
