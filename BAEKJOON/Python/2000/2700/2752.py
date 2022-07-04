"""
Title : 세수정렬
Link : https://www.acmicpc.net/problem/2752
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    print(*sorted(map(int, input().split())))
