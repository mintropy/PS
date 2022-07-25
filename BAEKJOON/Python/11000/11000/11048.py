from sys import stdin

'''
n, m = map(int, stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
'''

n, m  = 3, 4
graph = [[1,2,3,4],[0,0,0,5],[9,8,7,6]]


dp = [[0] * m for _ in range(n)]

dx, dy = [1, 1, 0], [0, 1, 1]

# 오른쪽 아래부터 왼쪽 위까지 dp 실행
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        tmp = []
        for k in range(3):
            nx, ny = i + dx[k], j + dy[k]
            if nx < n and ny < m:
                tmp.append(dp[nx][ny])
        if tmp == []:
            dp[i][j] = graph[i][j]
        else:
            dp[i][j] = max(tmp) + graph[i][j]

print(dp[0][0])