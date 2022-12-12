"""
Title : 냅색문제
Link : https://www.acmicpc.net/problem/1450
"""

from itertools import combinations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def solution(N: int, C: int, nums: list[int]) -> int:
    group1, group2 = [0], [0]
    mid = N // 2
    for i in range(1, mid + 1):
        for comb in combinations(nums[:mid], i):
            group1.append(sum(comb))
    for i in range(1, N - mid + 1):
        for comb in combinations(nums[mid:], i):
            group2.append(sum(comb))
    group1.sort()
    group2.sort()
    ans = 0
    idx = len(group1) - 1
    for y in group2:
        if y > C:
            break
        while idx >= 0:
            x = group1[idx]
            if x + y > C:
                idx -= 1
            else:
                break
        ans += idx + 1
    return ans


if __name__ == "__main__":
    N, C = MIIS()
    nums = sorted(MIIS())
    print(solution(N, C, nums))
