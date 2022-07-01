"""
Title : N번째 큰 수
Link : https://www.acmicpc.net/problem/2693
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        seq = sorted(map(int, input().split()))
        print(seq[7])
