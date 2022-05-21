"""
Title : 공장 컨설턴트 호석
Link : https://www.acmicpc.net/problem/22254
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def simulate(line_count: int) -> bool:
    global X, times
    line_times = [0] * line_count
    for time in times:
        heapq.heappushpop(line_times, line_times[0] + time)
    return True if max(line_times) <= X else False


def bin_search(N: int) -> int:
    global X
    left, right = 1, N
    while left <= right:
        mid = (left + right) // 2
        if simulate(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    N, X = MIIS()
    times = list(MIIS())
    print(bin_search(N))

'''
6 14
5 6 7 8 9 10
> 6

3 3
3 3 3
> 3
'''
