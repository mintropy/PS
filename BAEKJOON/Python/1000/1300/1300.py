"""
Title : K번째 수
Link : https://www.acmicpc.net/problem/1300
"""

import sys
input = sys.stdin.readline


def bin_search(n, k):
    left = 1
    right = n * n
    while left <= right:
        mid = (left + right) // 2
        cnt_smaller = 0
        cnt_same = 0
        for i in range(1, n + 1):
            # 하나하나씩 다 더하지 말고, 가능한 것의 수를 바로 더하자
            if mid // i >= n + 1:
                cnt_smaller += n
            elif mid // i <= n:
                cnt_smaller += mid //i
                if mid % i == 0:
                    cnt_same += 1
                    cnt_smaller -= 1
        if cnt_smaller < k and cnt_smaller + cnt_same >= k:
            return mid
        elif cnt_smaller + cnt_same < k:
            left = mid + 1
        else:
            right = mid - 1
    return mid


n = int(input())
k = int(input())

print(bin_search(n, k))