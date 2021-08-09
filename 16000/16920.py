"""
Title : 확장 게임
Link : https://www.acmicpc.net/problem/16920
"""

import sys
input = sys.stdin.readline


n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))

game_board = [list(input()) for _ in range(n)]
castle = [0] * (p + 1)

castle_check = [[] * (p + 1)]
for i in range(n):
    for j in range(m):
        try:
            k = int(game_board[i][j])
            castle[k] += 1
            castle_check[k] += 1
        except:
            continue


while True:
    if not castle_check:
        break


print(*castle)