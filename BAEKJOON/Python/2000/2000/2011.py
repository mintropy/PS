"""
Title : 암호코드
Link : https://www.acmicpc.net/problem/2011
"""

if __name__ == "__main__":
    N = [int(x) for x in input().strip()]
    if len(N) == 1:
        print(1)
        exit()
    mod = 1_000_000
    dp = [[0] * 2 for _ in range(len(N))]
    if N[0]:
        dp[0][0] = 1
    if N[1]:
        dp[-1][0] = 1
    for i in range(1, len(N)):
        if N[i]:
            dp[i][0] = sum(dp[i - 1]) % mod
        num = N[i - 1] * 10 + N[i]
        if N[i - 1] and 1 <= num <= 26:
            dp[i][1] = sum(dp[i - 2]) % mod
    if not N[-1]:
        dp[-1][0] = 0
    print(sum(dp[-1]) % mod)
