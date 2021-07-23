'''
Title : 네트워크 연결
Link : https://www.acmicpc.net/problem/1922
'''

import sys, collections

input = sys.stdin.readline

def bfs(a, b, tree):
    # a 점에서 시작, a점이 다시 나오면 False, 아니면 True 반환
    visited = [False] * (n + 1)
    queue = collections.deque([(b, 1)])
    visited[b] = True
    while queue:
        p, l = queue.popleft()
        for q in tree[p]:
            if q == a and l >= 2:
                return False
            if not visited[q]:
                queue.append((q, l + 1))
                visited[q] = True
    return True


n = int(input())
m = int(input())
cost = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    cost.append((c, a, b))
# cost.sort(key = lambda x: x[2])
cost.sort()
total_cost = 0

tree = [[] for _ in range(n + 1)]

for c, a, b in cost:
    if bfs(a, b, tree):
        tree[a].append(b)
        tree[b].append(a)
        total_cost += c

print(total_cost)