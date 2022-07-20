"""
Title : 10부제
Link : https://www.acmicpc.net/problem/10797
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    print(seq.count(N))
