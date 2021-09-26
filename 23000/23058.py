"""
Title : 뒤집기 게임
Link : https://www.acmicpc.net/problem/23058
"""

import sys
input = sys.stdin.readline

def dfs(pos, move):
    global n, board, min_move
    if pos == n ** 2:
        for i in range(n):
            if any(board[i]):
                return
        if move < min_move:
            min_move = move
        return
    if move > min_move:
        return
    x, y = pos // n, pos % n
    if not board[x][y]:
        dfs(pos + 1, move)
    # 가로로
    for i in range(n):
        for k in range(8):
            if board[x][k]:
                board[x][k] = 0
            else:
                board[x][k] = 1
        dfs(pos + 1, move + 1)
        for k in range(8):
            if board[x][k]:
                board[x][k] = 0
            else:
                board[x][k] = 1
    # 세로로
    for i in range(n):
        for k in range(8):
            if board[k][y]:
                board[k][y] = 0
            else:
                board[k][y] = 1
        dfs(pos + 1, move + 1)
        for k in range(8):
            if board[k][y]:
                board[k][y] = 0
            else:
                board[k][y] = 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

min_move = n
dfs(0, 0)
print(min_move)
