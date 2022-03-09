"""
Title : 고층 빌딩
Link : https://www.acmicpc.net/problem/1328
"""

import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, L, R = map(int, input().split())
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    dp[1][1][1] = 1
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i + 1):
                dp[i][j][k] = (dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i - 2)) % 1_000_000_007
    print(dp[N][L][R] % 1_000_000_007)

'''
DP 점화식
- 총 건물 N개, 왼쪽, 오른쪽에서 보이는 건물이 i, j 개일 때,
    - 점화식은 dp[N][i][j] = dp[N-1][i-1][j] + dp[N-1][i][j-1] + dp[N-1][i][j] * (N-2)
        - 가장 왼쪽, 오른쪽에 건물이 추가되는 경우
        - 중간에 건물이 추가되는 경우
'''
