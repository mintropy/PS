from sys import stdin

'''
n = int(stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
'''

n = 4
graph = [[2,3,3,1],[1,2,1,3],[1,2,3,1],[3,1,1,0]]


dp = [[0] * n for _ in range(n)]

# 오른쪽 아래부터 왼쪽 위까지 dp 실행
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if graph[i][j] == 0:
            continue
        x = graph[i][j]
        if j + x < n:
            if i == n - 1 and j + x == n - 1:
                dp[i][j] += 1
            else:
                dp[i][j] += dp[i][j + x]
        if i + x < n:
            if i + x == n - 1 and j == n - 1:
                dp[i][j] += 1
            else:
                dp[i][j] += dp[i + x][j]

print(dp[0][0])