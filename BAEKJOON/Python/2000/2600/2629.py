"""
Title :  양팔저울
Link : https://www.acmicpc.net/problem/2629
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = II()
    weights = sorted(MIIS())

    dp = [False] * 40_001
    weights_check = [set() for _ in range(40_001)]
    dp[0] = True
    for w in weights:
        for i in range(40_000, w - 1, -1):
            if dp[i - w]:
                dp[i] = True
                weights_check[i] |= {*weights_check[i - w], w}

    X = II()
    target = list(MIIS())
    ans = []
    for t in target:
        if dp[t]:
            ans.append("Y")
            continue
        for i in range(1, t):
            if t + i > 40_000:
                ans.append("N")
            if dp[t - i] and dp[t + i]:
                if weights_check[t - i] & weights_check[i]:
                    continue
                ans.append("Y")
                break
        else:
            ans.append("N")
    print(" ".join(ans))
