"""
Title : 거의 소수
Link : https://www.acmicpc.net/problem/1456
"""

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

is_prime = [True] * (int(b ** 0.5) + 2)
is_prime[1] = False
almost_prime = 0

for i in range(2, int(b ** 0.5) + 2):
    if is_prime[i]:
        power = i ** 2
        while True:
            if power > b:
                break
            elif power >= a:
                almost_prime += 1
            power *= i
        for j in range(i * 2, int(b ** 0.5) + 2, i):
            is_prime[j] = False

print(almost_prime)