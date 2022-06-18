"""
Title : 오븐 시계
Linkk : https://www.acmicpc.net/problem/2525
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    A, B = map(int, input().split())
    C = int(input())
    C += B
    A, B = A + C // 60, C % 60
    A %= 24
    print(A, B)
