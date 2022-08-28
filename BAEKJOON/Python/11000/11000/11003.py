"""
Title : 최솟값 찾기
Link : https://www.acmicpc.net/problem/11003
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, L = MIIS()
    seq = list(MIIS())
    ans = [0] * N
    queue = deque()
    for i, x in enumerate(seq):
        while queue and queue[-1][1] >= x:
            queue.pop()
        queue.append((i, x))
        while queue[0][0] < i - L + 1:
            queue.popleft()
        ans[i] = queue[0][1]
    print(*ans)
