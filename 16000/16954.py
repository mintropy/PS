"""
Title : 움직이는 미로 탈출
Link : https://www.acmicpc.net/problem/16954
"""

from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    walls = set()
    for i in range(8):
        chess_board = input()
        for j in range(8):
            if chess_board[j] == '#':
                walls.add((i, j))
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
    ans = 0
    pos = {(7, 0)}
    queue = deque([(7, 0, walls)])
    while queue:
        x, y, walls = queue.popleft()
        if x == 0 and y == 7:
            ans = 1
            break
        next_walls = {(x + 1, y) for x, y in walls if x < 7}
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx <= 7 and 0 <= ny <= 7:
                if (nx, ny) in walls or (nx, ny) in next_walls:
                    continue
                queue.append((nx, ny, next_walls))
    print(ans)
