"""
Title : 초콜릿 식사
Link : https://www.acmicpc.net/problem/2885
"""

from sys import stdin

input = stdin.readline


def find_num(K: int) -> int:
    n = 1
    while n < K:
        n *= 2
    return n


if __name__ == "__main__":
    K = int(input())
    n = find_num(K)
    if n == K:
        print(K, 0)
    else:
        ans = n
        count = 0
        while K:
            n //= 2
            K -= n
            count += 1
        print(ans, count)
