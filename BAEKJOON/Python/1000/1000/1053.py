"""
Title : 팰린드롬 공장
Link : https://www.acmicpc.net/problem/1053
"""

from sys import stdin

input = stdin.readline


def palindrome_factory(left: int, right: int) -> int:
    global s, dp
    if dp[left][right] != -1:
        return dp[left][right]
    if left >= right:
        return 0
    dp[left][right] = min(
        palindrome_factory(left + 1, right) + 1,
        palindrome_factory(left, right - 1) + 1,
        palindrome_factory(left + 1, right - 1) + (s[left] != s[right]),
    )
    return dp[left][right]


if __name__ == "__main__":
    s = list(input().strip())
    l = len(s)
    dp = [[-1] * l for _ in range(l)]
    ans = palindrome_factory(0, l - 1)
    for i in range(l - 1):
        for j in range(i + 1, l):
            s[i], s[j] = s[j], s[i]
            dp = [[-1] * l for _ in range(l)]
            ans = min(ans, palindrome_factory(0, l - 1) + 1)
            s[i], s[j] = s[j], s[i]
    print(ans)
