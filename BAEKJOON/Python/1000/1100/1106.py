"""
Title : 호텔
Link : https://www.acmicpc.net/problem/1106
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    C, N = MIIS()
    cities = [tuple(MIIS()) for _ in range(N)]

    people = [1_000_000] * (C + 1)
    for cost, p in cities:
        if people[p] > cost:
            people[p] = cost
    for i in range(1, C + 1):
        for j in range(1, i):
            for k in range():
                pass

    print(people)
