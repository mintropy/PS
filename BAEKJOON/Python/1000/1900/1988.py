"""
Title : 낮잠 시간
Link : https://www.acmicpc.net/problem/1988
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, B = map(int, input().split())
    seq = [int(input()) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N + 1)]
    