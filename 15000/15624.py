"""
Title :  피보나치 수 7
Link : https://www.acmicpc.net/problem/15624
"""

n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1_000_000_007
    print(b)
