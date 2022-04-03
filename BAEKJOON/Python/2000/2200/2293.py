from sys import stdin

'''
n, k = map(int, stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(stdin.readline()))
'''
n, k = 3, 10
coin = [1, 2, 5]


dp = [0] * (k + 1)

for i in range(n):
    cost = coin[i]
    for j in range(k + 1):
        if j == 0:
            dp[j] = 1
            continue
        if i == 0:
            if j % cost == 0:
                dp[j] = 1
            continue
        if cost <= j:
            dp[j] = dp[j] + dp[j - cost]

print(dp[-1])