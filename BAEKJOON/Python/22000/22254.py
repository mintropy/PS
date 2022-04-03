"""
Title : 공장 컨설턴트 호석
Link : https://www.acmicpc.net/problem/22254
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def simulate(X: int, line_count: int, times: list) -> int:
    line_times = [0] * line_count
    for time in times:
        heapq.heappushpop(line_times, line_times[0] + time)
        if line_times[0] > X:
            return X + 1
    return line_times[0]


def bin_search(N: int, X: int, times: list) -> int:
    total_time = sum(times)
    left, right = total_time // N - 1, N
    while left <= right:
        mid = (left + right) // 2
        if mid * X < total_time:
            left = mid + 1
        time_spend = simulate(X, mid, times)
        if time_spend <= X:
            right = mid - 1
        else:
            left = mid + 1
    return left


N, X = MIIS()
times = list(MIIS())

print(bin_search(N, X, times))

'''
5 14
5 6 7 8 9 10

'''