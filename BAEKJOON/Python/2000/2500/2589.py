"""
Title : 보물섬
Link : https://www.acmicpc.net/problem/2589
"""

from collections import deque
from sys import stdin


input = stdin.readline


def search():
    global max_dist, L, W, my_map
    delta = ((-1, 0, 1, 0), (0, 1, 0, -1))
    for i in range(L):
        for j in range(W):
            if my_map[i][j] == "W":
                continue
            queue = deque([(i, j, 0)])
            


if __name__ == "__main__":
    L, W = map(int, input().split())
    my_map = [input().strip() for _ in range(L)]
    max_dist = 0
