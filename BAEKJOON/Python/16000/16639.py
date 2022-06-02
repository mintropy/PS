"""
Title : 괄호 추가하기3
Link : https://www.acmicpc.net/problem/16639
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    dp = [0] * (N // 2 + 1)
