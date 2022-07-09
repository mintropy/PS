import sys
from itertools import combinations

input = lambda : sys.stdin.readline()

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
comb = list(combinations([i for i in range(n)], n // 2))
for i in range(len(comb) // 2):
    start = comb[i]
    link = comb[-1 -i]
    s, l = calculate_ability(start, link)
    if abs(s - l) < difference:
        difference = abs(s - l)

print(difference)