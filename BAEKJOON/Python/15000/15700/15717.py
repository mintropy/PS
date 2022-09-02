"""
Title : 떡파이어
Link : https://www.acmicpc.net/problem/15717
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    mod = 10 ** 9 + 7
    tmp = [1, 1]
    ans = 1
    while N  > 1:
        ans.append([ans[-1][0] * 2,])

