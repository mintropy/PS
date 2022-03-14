"""
Title : 흩날리는 시험지 속에서 내 평점이 느껴진거야
Link : https://www.acmicpc.net/problem/17951
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, K = MIIS()
    correct_counts = tuple(MIIS())
    left, right = N // K, (sum(correct_counts) // K) + 1
    ans = right
    while left <= right:
        mid = (left + right) // 2
        correct_sums = []
        tmp = 0
        for correct in correct_counts:
            tmp += correct
            if tmp >= mid:
                correct_sums.append(tmp)
                tmp = 0
        else:
            if tmp:
                correct_sums.append(tmp)
        if len(correct_sums) <= K:
            ans = min(correct_sums)
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
