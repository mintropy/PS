"""
Title : 문자판
Link : https://www.acmicpc.net/problem/2186
"""

from collections import deque
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    word_map = [input().strip() for _ in range(N)]
    target = input().strip()
    len_target = len(target)

    dp = [[[0] * M for _ in range(N)] for _ in range(len_target)]
    for i in range(N):
        for j in range(M):
            if word_map[i][j] == target[0]:
                dp[0][i][j] = 1
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for k in range(1, len_target):
        for i in range(N):
            for j in range(M):
                for dx, dy in delta:
                    for t in range(1, K + 1):
                        nx, ny = i + dx * t, j + dy * t
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if word_map[nx][ny] != target[k]:
                            continue
                        dp[k][nx][ny] += dp[k - 1][i][j]
    print(sum(sum(dp[-1], [])))
