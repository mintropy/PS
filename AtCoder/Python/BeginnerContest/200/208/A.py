import sys

input = sys.stdin.readline

a, b = map(int, input().split())
dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
for i in range(6):
    dp[1][i + 1] = 1


if a == 1 and b <= 6:
    print('Yes')
else:
    for i in range(2, a):
        for j in range(1, b):
            if j > 7:
                for k in range(1, 7):
                    if dp[i - 1][j - k] == 1:
                        dp[i][j] = 1
            else:
                for k in range(1, j):
                    if dp[i - 1][k] == 1:
                        dp[i][j] = 1
    if dp[-1][-1] == 1:
        print('Yes')
    else:
        print('No')