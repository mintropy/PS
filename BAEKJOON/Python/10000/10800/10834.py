"""
Title : 벨트
Link : https://www.acmicpc.net/problem/10834
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    M = int(input())

    ans = 1
    for _ in range(M):
        a, b, t = map(int, input().split())
        ans = (ans // a) * b
        if t:
            ans *= -1
    print(0 if ans > 0 else 1, abs(ans))
