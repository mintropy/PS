"""
Title : 나누기
Link : https://www.acmicpc.net/problem/1075
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())

if __name__ == "__main__":
    N, F = II(), II()
    _N = (N // 100) * 100
    if _N % F:
        print(str(_N + (F - _N % F))[-2:])
    else:
        print("00")
