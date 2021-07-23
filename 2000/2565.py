import sys

input = lambda : sys.stdin.readline()


n = int(input())
pole = [list(map(int, input().split())) for _ in range(n)]
pole.sort(key = lambda x: x[0])
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    min_value = 0
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            min_value = max(dp[j], min_value)
    dp[i] = min_value + 1

print(n - max(dp))