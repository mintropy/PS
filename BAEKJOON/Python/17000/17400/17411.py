"""
Title : 가장 긴 증가하는 부분 수열 6
Link : https://www.acmicpc.net/problem/17411
"""

from bisect import bisect_left
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = map(int, input().split())

    LIS = [next(seq)]
    max_sub_seq_len = 1
    max_sub_seq_count = 1
    for x in seq:
        if x > LIS[-1]:
            LIS.append(x)
            max_sub_seq_len += 1
            max_sub_seq_count = 1
        else:
            idx = bisect_left(LIS, x)
            if idx == max_sub_seq_len - 1:
                max_sub_seq_count += 1
            LIS[idx] = x
    print(max_sub_seq_len, max_sub_seq_count)
