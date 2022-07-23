import sys

input = sys.stdin.readline

n = int(input())
nuts = list(map(int, input().split()))

ans = 0
for i in range(n):
    if nuts[i] <= 10:
        continue
    ans += nuts[i] - 10

print(ans)