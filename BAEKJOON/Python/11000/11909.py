"""
Title : 배열 탈출
Link : https://www.acmicpc.net/problem/11909
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = [list(map(int, input().split())) for _ in range(n)]
