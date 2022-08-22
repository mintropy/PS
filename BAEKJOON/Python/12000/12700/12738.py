"""
Title : 가장 긴 증가하는 부분 수열 3
Link : https://www.acmicpc.net/problem/12738
"""

from sys import stdin
from bisect import bisect_left

input = stdin.readline


if __name__ == "__main__":
    A = int(input())
    seq = map(int, input().split())

    LIS = [next(seq)]
    for x in seq:
        if x > LIS[-1]:
            LIS.append(x)
        else:
            LIS[bisect_left(LIS, x)] = x
    print(len(LIS))
