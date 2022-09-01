"""
Title : 개수 세기
Link : https://www.acmicpc.net/problem/10807
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    V = int(input())
    print(seq.count(V))
