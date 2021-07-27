"""
Title : IQ Test
Link : https://www.acmicpc.net/problem/1111
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))



if n == 2:
    print('A')
elif n == 3:
    a = (seq[2] - seq[1]) // (seq[1] - seq[0])
    b = seq[2] - a * seq[0]
    
