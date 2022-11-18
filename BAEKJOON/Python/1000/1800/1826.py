"""
Title : 연료 채우기
Link : https://www.acmicpc.net/problem/1826
"""

from heapq import heappop, heappush
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search(N: int, gas_stations: list[tuple[int]], L: int, P: int) -> int:
    heap = [(0, -1, P)]
    while heap:
        x, idx, gas = heappop(heap)
        pos = gas_stations[idx][0]
        max_pos = pos + gas
        if max_pos >= L:
            return x
        for i in range(idx + 1, N):
            next_pos, next_gas = gas_stations[i]
            if max_pos < next_pos:
                break
            heappush(heap, (x + 1, i, gas - (next_pos - pos) + next_gas))
    return -1


if __name__ == "__main__":
    N = int(input())
    gas_stations = sorted([tuple(MIIS()) for _ in range(N)]) + [(0, 0)]
    L, P = MIIS()
    print(search(N, gas_stations, L, P))
