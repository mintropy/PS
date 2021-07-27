"""
Title : 나무 자르기
Link : https://www.acmicpc.net/problem/2805
"""

# 종료조건, 반환값이 이상한 듯?

import sys

input = sys.stdin.readline

def bin_search(m, trees):
    # 자른 높이, 가져가는 길이
    close = [0, sum(trees)]
    minimum = 1
    maximum = max(trees)
    mid = maximum // 2
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        count = sum(tree - mid if tree > mid else 0 for tree in trees)
        # 정확한 개수를 모았을 때
        if count == m:
            break
        # 탐색 실패 대비
        if count > m and count < close[1]:
            close = [mid, count]
        # 다음 이분 탐색
        if count > m:
            minimum = mid + 1
        elif count < m:
            maximum = mid - 1
    if count < m or m < close[1] < count:
        return close[0]
    else:
        return mid


n, m = map(int, input().split())
trees = sorted((map(int, input().split())), reverse = True)

print(bin_search(m, trees))