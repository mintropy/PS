"""
Title : 속타는 저녁 메뉴
Link : https://www.acmicpc.net/problem/11585
"""

from math import gcd
from sys import stdin

input = stdin.readline


def get_lps(N: int, target: list):
    lps = [0] * N
    idx = 1
    len_idx = 0
    while idx < N:
        if target[idx] == target[len_idx]:
            len_idx += 1
            lps[idx] = len_idx
            idx += 1
        else:
            if len_idx:
                len_idx = lps[len_idx - 1]
            else:
                idx += 1
    return lps


def kmp(N: int, roulette: list, target: list, lps: list):
    count = 0
    idx = target_idx = 0
    while idx < N * 2 - 1:
        if roulette[idx] == target[target_idx]:
            idx += 1
            target_idx += 1
        else:
            if target_idx:
                target_idx = lps[target_idx - 1]
            else:
                idx += 1
        if target_idx == N:
            count += 1
            target_idx = lps[target_idx - 1]
    return count


if __name__ == "__main__":
    N = int(input())
    roulette = list(input().strip().split())
    target = list(input().strip().split())
    if roulette == roulette[0] * N:
        print("1/1")
        exit()
    lps = get_lps(N, target)
    count = kmp(N, roulette + roulette, target, lps)
    g = gcd(N, count)
    print(f"{count // g}/{N // g}")
