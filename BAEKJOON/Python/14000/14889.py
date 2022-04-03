import sys

input = lambda : sys.stdin.readline()

# dfs 탐색
def dfs(start, link, idx):
    global n, difference
    if idx == n:
        s, l = calculate_ability(start, link)
        if abs(s - l) < difference:
            difference = abs(s - l)
        return
    if len(start) < n // 2:
        start.append(idx)
        dfs(start, link, idx + 1)
        start.pop(-1)
    if len(link) < n // 2:
        link.append(idx)
        dfs(start, link, idx + 1)
        link.pop(-1)
    
# 두 팀으로 구분되었을 때, 각 팀 능력치 계산
def calculate_ability(start, link):
    global n
    s, l = 0, 0
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j:
                continue
            s += ability[start[i]][start[j]]
            l += ability[link[i]][link[j]]
    return s, l


n = int(input())
ability = []
for _ in range(n):
    ability.append(list(map(int, input().split())))

difference = sys.maxsize
start, link = [], []
dfs(start, link, 0)
print(difference)