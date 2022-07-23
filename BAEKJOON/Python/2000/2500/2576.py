"""
Title : 홀수
Link : https://www.acmicpc.net/problem/2576
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    odd_sum = 0
    min_odd = 101
    for _ in range(7):
        n = int(input())
        if n % 2:
            odd_sum += n
            min_odd = min(min_odd, n)
    if odd_sum:
        print(odd_sum, min_odd, sep="\n")
    else:
        print(-1)
