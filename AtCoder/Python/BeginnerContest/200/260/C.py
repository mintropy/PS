N, X, Y = map(int, input().split())

reds = [0] * 11
reds[N] += 1
blues = [0] * 11

for i in range(N, 1, -1):
    reds[i - 1] += reds[i]
    blues[i] += reds[i] * X
    reds[i - 1] += blues[i]
    blues[i - 1] += blues[i] * Y

print(blues[1])
