"""
Title : 공사장 표지판
Link : 
"""

n = int(input())

board = [[' '] * n for  _ in range(n)]

# 테두리
for i in range(n):
    board[0][i] = '*'
    board[n - 1][i] = '*'
    board[i][0] = '*'
    board[i][n - 1] = '*'

# 중간
for i in range(0, n - 2):
    board[1 + i][1 + i] = '*'
    board[n - 2 - i][1 + i] = '*'

for line in board:
    print(''.join(line))
