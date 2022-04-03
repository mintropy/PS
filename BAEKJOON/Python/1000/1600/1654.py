"""
Title : 랜선 자르기
Link : https://www.acmicpc.net/problem/1654
"""

import sys
input = sys.stdin.readline

def bin_search(n, lines):
    left = 0
    right = max(lines)
    possible = 0
    while left <= right:
        mid = (left + right) // 2
        if mid != right:
            mid += 1
        # 렌선 개수
        count = 0
        if mid == 0:
            count = len(lines)
        else:
            for line in lines:
                count += line // mid
        if count < n:
            right = mid - 1
        # elif count >= n:
        else:
            if possible < mid:
                possible = mid
            left = mid + 1
    return possible


k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]


print(bin_search(n, lines))