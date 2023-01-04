"""
Title : 사다리 조작
Link : https://www.acmicpc.net/problem/15684
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search(count: int) -> int:
    global N, H, my_map, ans
    if count >= ans:
        return ans
    for i in range(H):
        for j in range(N):
            if my_map[i][j]:
                continue
            my_map[i][j] = True
            search(count + 1)
            my_map[i][j] = False


def check() -> bool:
    global my_map
    for j in range(N):
        idx = j


if __name__ == "__main__":
    N, M, H = MIIS()
    my_map = [[False] * N for _ in range(H)]
    for _ in range(M):
        a, b = MIIS()
        my_map[a - 1][b - 1] = True
    ans = 1000
