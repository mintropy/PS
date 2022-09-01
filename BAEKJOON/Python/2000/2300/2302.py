"""
Title : 극장 좌석
Link : https://www.acmicpc.net/problem/2302
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    N: int = II()
    M: int = II()
    vips: list[int] = [II() for _ in range(M)] + [N + 1]

    dp: list[list[int]] = [[0] * 2 for _ in range(N + 1)]
    dp[0] = [1, 0]
    vip_idx: int = 0
    last_vip: bool = True
    for i in range(1, N + 1):
        if i == vips[vip_idx]:
            dp[i] = dp[i - 1]
            vip_idx += 1
            last_vip = True
            continue
        if last_vip:
            dp[i] = dp[i - 1]
            last_vip = False
        else:
            dp[i] = [sum(dp[i - 1]), dp[i - 1][0]]
    print(sum(dp[-1]))
