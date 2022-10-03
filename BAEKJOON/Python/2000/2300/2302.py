"""
Title : 극장 좌석
Link : https://www.acmicpc.net/problem/2302
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


def solve(N: int, M: int, seats: list[int]) -> int:
    dp = [0] * (41)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    seats += [0, N + 1]
    seats.sort()
    ans = 1
    for i in range(M + 1):
        x, y = seats[i], seats[i + 1]
        ans *= dp[y - x - 1]
    return ans


if __name__ == "__main__":
    N: int = II()
    M: int = II()
    vips: list[int] = [II() for _ in range(M)] + [N + 1]
    print(solve(N, M, vips))
