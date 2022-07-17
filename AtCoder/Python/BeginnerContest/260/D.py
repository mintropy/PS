MIIS = lambda: map(int, input().split())

N, K = MIIS()
cards = list(MIIS())
ans = [-1] * N

print(*ans, sep="\n")
