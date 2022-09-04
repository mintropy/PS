"""
Title : 택배
Link : https://www.acmicpc.net/problem/8980
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N: int
    C: int
    N, C = MIIS()
    M: int = int(input())
    boxex: list[tuple[int]] = [tuple(MIIS()) for _ in range(M)]
    boxex.sort(key=lambda x: x[1])

    truck_available: list[int] = [C] * (N + 1)
    ans = 0
    for st, end, w in boxex:
        available = min(w, min(truck_available[st:end]))
        for i in range(st, end):
            truck_available[i] -= available
        ans += available

    print(ans)
