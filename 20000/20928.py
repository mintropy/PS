"""
Title : 걷는 건 귀찮아
Link : https://www.acmicpc.net/problem/20928
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int , input().split())


if __name__ == '__main__':
    N, M = MIIS()
    positions = list(MIIS())
    moves = list(MIIS())

    dp = [-1] * (M + 1)
    count = 0
    for i in range(positions[0], min(M + 1, positions[0] + moves[0])):
        dp[i] = 0
    next_pos = positions[0] + moves[0] + 1

    for idx, pos in enumerate(positions[1:]):
        if dp[pos] == -1:
            break
        if next_pos < pos + moves[idx]:
            tmp = min(M + 1, pos + moves[idx])
            for i in range(next_pos, tmp):
                dp[i] = dp[pos] + 1
            next_pos = tmp + 1
    print(dp[M])
