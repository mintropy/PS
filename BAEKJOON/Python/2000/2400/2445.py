"""
Title : 별 찍기 - 8
Link : https://www.acmicpc.net/problem/2445
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    output = ""
    for i in range(1, N + 1):
        output += "*" * i + " " * (N - i) + " " * (N - i) + "*" * i + "\n"
    for i in range(N - 1, 0, -1):
        output += "*" * i + " " * (N - i) + " " * (N - i) + "*" * i + "\n"
    print(output)
