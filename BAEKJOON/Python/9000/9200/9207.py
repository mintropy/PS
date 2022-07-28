"""
Title : 페그 솔리테어
Link : https://www.acmicpc.net/problem/9207
"""

from sys import stdin
input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        game_board = list(input().strip() for _ in range(5))
        
        
        if i == N - 1:
            break
        input()
