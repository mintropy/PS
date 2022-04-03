'''
Title : 오목 판정
'''

def check_row(board, i, j):
    for k in range(1, 5):
        if board[i][j + k] == '.':
            return False
    return True

def check_col(board, i, j):
    for k in range(1, 5):
        if board[i + k][j] == '.':
            return False
    return True

def check_dia(board, i, j):
    for k in range(1, 5):
        if board[i + k][j + k] == '.':
            return False
    return True

def check_reverse_dia(board, i, j):
    for k in range(1, 5):
        if board[i - k][j + k] == '.':
            return False
    return True

def is_omok(n, board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                continue
            if i >= 4 and n - j >= 5:
                if check_reverse_dia(board, i, j):
                    return True
            if n - i >= 5 and n - j >= 5:
                if check_col(board, i, j) or check_row(board, i, j) or check_dia(board, i, j):
                    return True
            elif n - i >= 5:
                if check_col(board, i, j):
                    return True
            elif n - j >= 5:
                if check_row(board, i, j):
                    return True
    return False

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    board = [str(input()) for _ in range(n)]
    if is_omok(n, board):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')