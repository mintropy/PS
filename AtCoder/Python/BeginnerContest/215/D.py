import sys, itertools
input = sys.stdin.readline


def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


n, m = map(int, input().split())
seq = list(map(int, input().split()))
num_check = [True] * (m + 1)

ans = [1]
for i in range(2, m + 1):
    if not num_check[i]:
        continue
    for num in seq:
        if gcd(i, num) != 1:
            break
    else:
        ans.append(i)
        for j in range(i * 2, m + 1, i):
            num_check[j] = False

print(len(ans), *ans, sep = '\n')
