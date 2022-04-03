"""
Title : 2021은 무엇이 특별할까?
Link : https://www.acmicpc.net/problem/24039
"""

import sys
input = sys.stdin.readline


N = int(input())
primes = []
is_prime = [True] * 201
for i in range(2, 201):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, 201, i):
            is_prime[j] = False

special_nums = [-1]
for i in range(len(primes) - 1):
    tmp = primes[i] * primes[i + 1]
    if special_nums[-1] == N or special_nums[-1] < N < tmp:
        print(tmp)
        break
    else:
        special_nums.append(primes[i] * primes[i + 1])
