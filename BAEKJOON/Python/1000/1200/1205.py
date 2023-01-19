"""
Title : 등수 구하기
Link : https://www.acmicpc.net/problem/1205
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, ts, P = MIIS()
    scores = tuple(MIIS())

    places = []
    for i, x in enumerate(scores):
        if not places or places[-1][2] != x:
            places.append((i, x))

    if N == 0 or ts >= scores[0]:
        print(1)
    elif ts < scores[-1]:
        if N < P:
            print(N + 1)
        else:
            print(-1)
    else:
        for i, x in places:
            pass

    if N == 0:
        print(1)
    elif ts >= scores[0]:
        print(1)
    elif ts <= scores[-1] and N == P:
        print(-1)
    elif ts == scores[-1]:
        print(N)
    elif ts < scores[-1]:
        print(N + 1)
    else:
        for i, x in enumerate(scores):
            if ts >= x:
                print(i + 1)
                break
