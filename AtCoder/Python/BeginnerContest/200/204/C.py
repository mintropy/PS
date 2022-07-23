import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
city = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if city[i][j] == 1:
                continue
            if city[i][k] + city[k][j] == 2:
                city[i][j] = 1

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            ans += 1
            continue
        if city[i][j] == 1:
            ans += 1
            continue
print(ans)