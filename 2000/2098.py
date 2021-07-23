import sys

input = sys.stdin.readline

def TSP(dp: list, visit: int, now: int):
    global n, w, ans
    # 모든 점을 방문 했을 때
    if visit == ((1 << n) - 1):
        weight = dp[now][-1] + w[now][0]
        if weight < ans:
            ans = weight
        return
    # 방문하지 않은 점을 찾아서 방문
    for i in range(1, n):
        if not (visit & (1 << i)):
            visit2 = visit | (1 << i)
            dp[i][visit2] = min(dp[i][visit2], dp[now][visit] + w[now][i])
            TSP(dp, visit2, i)

n = int(input())
INF = int(1e10)
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][1] = 0
ans = INF
TSP(dp, 1, 0)
print(ans)
