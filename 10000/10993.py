"""
Title : 별 찍기 - 18
Link : https://www.acmicpc.net/problem/10993
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    ans = ['*']
    for _ in range(N - 1):
        next_ans = []
