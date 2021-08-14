"""
Title :  숫자 카드
Link : https://www.acmicpc.net/problem/10815
"""

import sys
input = sys.stdin.readline


def bin_search(card: list, k: int) -> int:
    st, end = 0, n - 1
    while st <= end:
        mid = (st + end) // 2
        if card[mid] == k:
            return 1
        elif card[mid] > k:
            end = mid - 1
        else:
            st = mid + 1
    return 0


n = int(input())
card = sorted(list(map(int, input().split())))

m = int(input())
target = list(map(int, input().split()))
for k in target:
    print(bin_search(card, k), end = ' ')
