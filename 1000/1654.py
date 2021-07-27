"""
Title : 랜선 자르기
Link : https://www.acmicpc.net/problem/1654
"""

import sys
input = sys.stdin.readline

def bin_search(n, lines):
    left = 0
    right = max(lines)
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for line in lines:
            count += line // mid
        if count < n:
            right = mid - 1
        elif count == n:
            if left == mid:
                break
            left = mid
        else:
            if left == mid:
                break
            left = mid
    return mid


k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]


print(bin_search(n, lines))