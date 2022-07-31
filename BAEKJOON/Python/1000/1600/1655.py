"""
Title : 가운데를 말해요
Link : https://www.acmicpc.net/problem/1655
"""

import heapq
from sys import stdin

input = stdin.readline
II = lambda: int(input())


def adjust_heap():
    global mid, small_val, large_val
    while True:
        if len(small_val) == len(large_val) or len(small_val) + 1 == len(large_val):
            return
        if len(small_val) > len(large_val):
            mid, tmp = -heapq.heappop(small_val), mid
            heapq.heappush(large_val, tmp)
        else:
            tmp, mid = mid, heapq.heappop(large_val)
            heapq.heappush(small_val, -tmp)


if __name__ == "__main__":
    N = II()
    mid = II()
    ans = f"{mid}\n"
    small_val, large_val = [], []
    for i in range(1, N):
        k = II()
        if k >= mid:
            heapq.heappush(large_val, k)
        else:
            heapq.heappush(small_val, -k)
        adjust_heap()
        ans += f"{mid}\n"
    print(ans)

"""
4
2
3
4
1
ans 2 2 3 2
"""
