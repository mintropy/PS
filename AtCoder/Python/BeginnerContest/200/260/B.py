MIIS = lambda: map(int, input().split())

N, X, Y, Z = MIIS()
math = list(MIIS())
english = list(MIIS())
sum_scores = [math[i] + english[i] for i in range(N)]
check = [False] * N
ans = []

math_highest = sorted(
    [(s, idx) for idx, s in enumerate(math)], key=lambda x: (-x[0], x[1])
)
for i in range(X):
    _, idx = math_highest[i]
    ans.append(idx + 1)
    check[idx] = True

english_highest = sorted(
    [(s, idx) for idx, s in enumerate(english)], key=lambda x: (-x[0], x[1])
)
for i in range(N):
    if not Y:
        break
    _, idx = english_highest[i]
    if check[idx]:
        continue
    Y -= 1
    ans.append(idx + 1)
    check[idx] = True

sum_highest = sorted(
    [(s, idx) for idx, s in enumerate(sum_scores)], key=lambda x: (-x[0], x[1])
)
for i in range(N):
    if not Z:
        break
    _, idx = sum_highest[i]
    if check[idx]:
        continue
    Z -= 1
    ans.append(idx + 1)
    check[idx] = True

print(*sorted(ans), sep="\n")
