"""
Title : 줄세우기
Link : https://www.acmicpc.net/problem/2631
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


def solve(N: int, num: list[int]) -> int:
    dp = [1] * N
    for i, x in enumerate(num):
        for j in range(i):
            if num[j] < x and (tmp := dp[j] + 1) > dp[i]:
                dp[i] = tmp
    return N - max(dp)


if __name__ == "__main__":
    N = II()
    nums = [II() for _ in range(N)]
    print(solve(N, nums))
