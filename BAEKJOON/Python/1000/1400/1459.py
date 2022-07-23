"""
Title : 걷기
Link : https://www.acmicpc.net/problem/1459
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    X, Y, W, S = map(int, input().split())
    min_val, max_val = min(X, Y), max(X, Y)
    dist = 0
    if S < W * 2:
        dist += min_val * S
        if S < W:
            dist += ((max_val - min_val) // 2) * 2 * S
            dist += ((max_val - min_val) % 2) * W
        else:
            dist += (max_val - min_val) * W
    else:
        dist += (X + Y) * W
    print(dist)

"""
현재 (0, 0) -> (X, Y)
도로를 따라서 or 대각선 가로질러

한 블록 W, 대각선 S
"""
