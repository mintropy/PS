"""
Title : 나무 자르기
Link : https://www.acmicpc.net/problem/2805
"""

# 종료조건, 반환값이 이상한 듯?

import sys

input = sys.stdin.readline

def bin_search(m, trees):
    minimum = 1
    maximum = max(trees)
    mid = maximum // 2
    while minimum < maximum:
        mid = (minimum + maximum) // 2
        count = sum(tree - mid if tree > mid else 0 for tree in trees)
        if count == m:
            break
        elif count > m:
            minimum = mid + 1
        elif count < m:
            maximum = mid - 1
    return max(maximum, minimum)


n, m = map(int, input().split())
trees = sorted((map(int, input().split())), reverse = True)

print(bin_search(m, trees))