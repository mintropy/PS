from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    
    if (ax + ay) % 2 != (bx + by) % 2:
        print(-1)
        exit()
    
    chess_board = [list(input().strip()) for _ in range(N)]
    queue = deque([(ax - 1, ay - 1, 0)])
    dx, dy = (-1, -1, 1, 1), (-1, 1, 1, -1)
    while queue:
        x, y, m = queue.popleft()
        if type(chess_board[x][y]) == int and chess_board[x][y] <= m:
            continue
        chess_board[x][y] = m
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            while True:
                if 0 <= nx < N and 0 <= ny < N:
                    if chess_board[nx][ny] == '.':
                        queue.append((nx, ny, m + 1))
                        nx, ny = nx + dx[d], ny + dy[d]
                        continue
                break
    if chess_board[bx - 1][by - 1] == '.':
        print(-1)
    else:
        print(chess_board[bx - 1][by - 1])