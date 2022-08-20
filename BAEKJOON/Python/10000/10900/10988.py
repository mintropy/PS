"""
Title : 팰린드롬인지 확인하기
Link : https://www.acmicpc.net/problem/10988
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    s = input().strip()
    if s == s[::-1]:
        print(1)
    else:
        print(0)
