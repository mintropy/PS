"""
Title : 일루미네이션
Link : https://www.acmicpc.net/problem/5547
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    W, H = MIIS()
    walls = [list(MIIS()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    delta = {
        "hexagon": [(0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1)],
        "vertex_up": [(0, -1), (-1, -1), (1, 1)],
        "vertax_down": [(0, 1), (-1, -1), (1, -1)],
    }
    dist = 0
    for i in range(H):
        for j in range(W):
            if not walls[i][j] or visited[i][j]:
                continue
            st = (i, j)
            
    print(dist)
