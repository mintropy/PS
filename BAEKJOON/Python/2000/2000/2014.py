"""
Title : 소수의 곱
Link : https://www.acmicpc.net/problem/2014
"""

from heapq import heappush, heappop
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    K, N = MIIS()
    primes = list(MIIS())
    heap = primes[::]
    count = 0
    while count < N:
        x = heappop(heap)
        count += 1
        if count == N:
            print(x)
            break
        for i in range(K - 1, -1, -1):
            y = primes[i]
            if x % y:
                continue
            for j in range(i, K):
                heappush(heap, x * primes[j])
            break
