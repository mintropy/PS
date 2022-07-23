import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
tastiness = list(MIIS())
dislikes_food = list(MIIS())

best = max(tastiness)
ans = "No"
for idx in dislikes_food:
    if tastiness[idx - 1] == best:
        ans = "Yes"
        break

print(ans)
