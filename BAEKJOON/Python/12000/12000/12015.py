"""
Title : 가장 긴 증가하는 부분 수열 2
Link : https://www.acmicpc.net/problem/12015
"""

from sys import stdin
from bisect import bisect_left

input = stdin.readline


if __name__ == "__main__-":
    A = int(input())
    seq = map(int, input().split())

    LIS = [next(seq)]
    for x in seq:
        if x > LIS[-1]:
            LIS.append(x)
        else:
            LIS[bisect_left(LIS, x)] = x
    print(len(LIS))


def bin_search(x: int, LIS: list[int]) -> int:
    left, right = 0, len(LIS) - 1
    while left < right:
        mid = (left + right) // 2
        if LIS[mid] < x:
            left = mid + 1
        else:
            right = mid
    return right


if __name__ == "__main__":
    A = int(input())
    seq = map(int, input().split())

    LIS = [next(seq)]
    for x in seq:
        if x > LIS[-1]:
            LIS.append(x)
        else:
            LIS[bin_search(x, LIS)] = x
    print(len(LIS))
