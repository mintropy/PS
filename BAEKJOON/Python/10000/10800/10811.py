"""
title : 바구니 뒤집기
link : https://www.acmicpc.net/problem/10811
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    basket = [i for i in range(1, n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        basket[i - 1 : j] = basket[i - 1 : j][::-1]
    print(*basket)
