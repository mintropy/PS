"""
Title : 그림
Link : https://www.acmicpc.net/problem/1926
"""

from sys import stdin

input = stdin.readline


class BFS:
    def __init__(self, board: list[list[int]], n: int, m: int) -> None:
        self.board = board
        self.n = n
        self.m = m
        self.visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]
        self.delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.pieces = 0
        self.max_size = 0

    def search(self) -> None:
        for i in range(1, len(self.board) - 1):
            for j in range(1, len(self.board[0]) - 1):
                if self.board[i][j] == 1 and not self.visited[i][j]:
                    self.pieces += 1
                    self.max_size = max(self.max_size, self.bfs(i, j))

    def bfs(self, x: int, y: int) -> int:
        size = 1
        self.visited[x][y] = True
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in self.delta:
                nx, ny = x + dx, y + dy
                if self.board[nx][ny] == 1 and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    size += 1
                    queue.append((nx, ny))
        return size


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    board = [[0] * (m + 2)] + [[0] + i + [0] for i in board] + [[0] * (m + 2)]

    bfs = BFS(board, n, m)
    bfs.search()
    print(f"{bfs.pieces }\n{bfs.max_size}")
