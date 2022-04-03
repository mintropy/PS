"""
Title : 저작권
Link : https://www.acmicpc.net/problem/2914
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, I = map(int, input().split())
    print(A * (I - 1) + 1)
