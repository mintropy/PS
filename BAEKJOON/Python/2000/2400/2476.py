"""
Title : 주사위 게임
Link : https://www.acmicpc.net/problem/2476
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    answer = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        if a == b == c:
            tmp = 10000 + a * 1000
        elif a == b:
            tmp = 1000 + 100 * a
        elif b == c:
            tmp = 1000 + 100 * b
        elif c == a:
            tmp = 1000 + 100 * c
        else:
            tmp = max(a, b, c) * 100
        if answer < tmp:
            answer = tmp
    print(answer)
