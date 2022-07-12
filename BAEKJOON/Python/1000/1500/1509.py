"""
Title : 팰린드롬 분할
Link : https://www.acmicpc.net/problem/1509
"""

from sys import stdin
input = stdin.readline


if __name__ == "__main__":
    s = input().strip()
    l = len(s)
    dp = [0] * l
