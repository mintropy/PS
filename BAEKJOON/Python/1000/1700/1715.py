"""
Title : 카드 정렬하기
Link : https://www.acmicpc.net/problem/1715
"""

import heapq
from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    N = int(input())
    cards = [II() for _ in range(N)]
    heapq.heapify(cards)

    ans = 0
    while len(cards) > 1:
        x, y = heapq.heappop(cards), heapq.heappop(cards)
        ans += x + y
        heapq.heappush(cards, x + y)
    print(ans)
