"""
Title : 색종이 올려 놓기
Link : https://www.acmicpc.net/problem/2643
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    papers = [tuple(map(int, input().split())) for _ in range(N)]
    papers.sort(reverse=True, key=lambda x: x[0] * x[1])

    dp = [1] * N
    for i in range(1, N):
        x2, y2 = papers[i]
        for j in range(i):
            x1, y1 = papers[j]
            if (x1 >= x2 and y1 >= y2) or (x1 >= y2 and y1 >= x2):
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    print(max(dp))
