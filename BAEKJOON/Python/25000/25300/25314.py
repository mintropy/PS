"""
Title : 코딩은 체육과목 입니다
Link : https://www.acmicpc.net/problem/25314
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    print(" ".join(["long" for _ in range(N // 4)]), "int")
