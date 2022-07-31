"""
Title : 가운데를 말해요
Link : https://www.acmicpc.net/problem/1655
"""

from heapq import heappush, heappushpop
from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    N = II()
    mid = II()
    ans = f"{mid}\n"
    small_val, large_val = [], []
    for i in range(1, N):
        k = II()
        if i % 2:
            if k < mid:
                heappush(large_val, mid)
                mid = -heappushpop(small_val, -k)
            else:
                heappush(large_val, k)
        else:
            if k > mid:
                heappush(small_val, -mid)
                mid = heappushpop(large_val, k)
            else:
                heappush(small_val, -k)
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
