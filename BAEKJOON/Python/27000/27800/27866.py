"""
Title : 문자와 문자열
Link : https://www.acmicpc.net/problem/27866
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    S = input().strip()
    i = int(input())

    print(S[i - 1])
