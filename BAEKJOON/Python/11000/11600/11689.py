"""
Title : GCD(n, k) = 1
Link : https://www.acmicpc.net/problem/11689
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            ans = (ans // i) * (i - 1)
            while not n % i:
                n //= i
        if n == 1:
            break
    print(ans if n == 1 else (ans // n) * (n - 1))
