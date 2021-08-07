"""
Title : 네 개의 소수
Link : https://www.acmicpc.net/problem/1153
"""

n = int(input())

is_prime = [True] * (n + 1)
primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False


if n < 8:
    print(-1)
else:
    if n % 2 == 0:
        a = b = 2
    else:
        a, b = 2, 3
    
    n -= (a + b)
    
    for p in primes:
        if n - p in primes:
            break
    
    print(a, b, p, n - p)