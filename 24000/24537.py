"""
Title : 약수 계산
Link : https://www.acmicpc.net/problem/24537
"""

import sys
input = sys.stdin.readline


if __name__=='__main__':
    N = int(input())
    nums = sorted(map(int, input().split()))
    Q = int(input())
    
    is_prime = [True] * 317
    primes = []
    for i in range(2, 317):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, 317, i):
                is_prime[j] = False
    
    count = [-1] * 100_001
    
    
    
    for _ in range(Q):
        K = int(input())
        print(count[K])
