"""
Title : 파괴된 도시
Link : https://www.acmicpc.net/problem/18231
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
roads = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    roads[u].append(v)
    roads[v].append(u)

k = int(input())
destroyed = tuple(map(int, input().split()))

# 파괴된 도시는 0, 아니면 1로
city = [1] * (n + 1)
for dt in destroyed:
    city[dt] = 0

bomb = set()
destroyed_check = set()
# 파괴된 도시와 연결된 도시가 모두 파괴되었으면
# 해당 도시와 주변도시를 모두 check에 추가
# 중심 도시는 bomb에 추가
for dt in destroyed:
    for next_city in roads[dt]:
        if city[next_city]:
            break
    else:
        bomb.add(dt)
        destroyed_check.update([dt] + roads[dt])

bomb = list(bomb)
destroyed_check = list(destroyed_check)

if len(destroyed) == len(destroyed_check):
    print(len(bomb))
    print(*bomb)
else:
    print(-1)
