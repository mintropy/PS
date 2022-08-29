"""
Title : 과자
Link : https://www.acmicpc.net/problem/10156
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    K: int
    N: int
    M: int

    K, N, M = map(int, input().split())
    print(max(0, K * N - M))
