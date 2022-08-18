"""
Title : 원 영역
Link : https://www.acmicpc.net/problem/10000
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    circles = []
    for _ in range(N):
        x, r = map(int, input().split())
        circles.append((x - r, x + r))
    circles.sort(key=lambda x: (x[0], -x[1]))
    ans = 0
    stack = []
    for l, r in circles:
        if not stack:
            stack.append((l, r))
            continue
        if r < stack[0][1]:
            pass
        else:
            pass
