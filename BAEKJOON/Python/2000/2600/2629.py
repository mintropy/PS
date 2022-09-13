"""
Title :  양팔저울
Link : https://www.acmicpc.net/problem/2629
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


def search(idx: int, weight: int) -> None:
    global N, weights, dp
    if idx > N or dp[idx][weight]:
        return
    dp[idx][weight] = True
    search(idx + 1, weight + weights[idx])
    search(idx + 1, abs(weight - weights[idx]))
    search(idx + 1, weight)


if __name__ == "__main__":
    N = II()
    weights = list(MIIS()) + [0]
    dp = [[False] * 40_001 for _ in range(31)]
    search(0, 0)

    X = II()
    target = list(MIIS())
    ans = " ".join(["Y" if dp[N][t] else "N" for t in target])
    print(ans)
