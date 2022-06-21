"""
Title : 수들의 합
Link : https://www.acmicpc.net/problem/1789
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    ans = 1
    while True:
        if N < (ans + 1) * (ans + 2) // 2:
            print(ans)
            break
        ans += 1
