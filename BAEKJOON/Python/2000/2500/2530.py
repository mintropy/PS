"""
Title : 인공지능 시계
Link : https://www.acmicpc.net/problem/2530
"""

from sys import stdin
input = stdin.readline


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    D = int(input())
    now = A * 60 * 60 + B * 60 + C
    end = now + D
    end %= 24 * 60 * 60
    H, M, S = (end // (60 * 60)) % 24, (end % (60 * 60)) // 60, end % 60
    print(H, M, S)
