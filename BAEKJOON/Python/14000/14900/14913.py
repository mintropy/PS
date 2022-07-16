"""
Title : 등차수열에서 항 번호 찾기
Link : https://www.acmicpc.net/problem/14913
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    a, d, k = map(int, input().split())
    diff = k - a
    if diff * d < 0 or diff % d:
        print("X")
    else:
        print(diff // d + 1)
