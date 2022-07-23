import sys
input = sys.stdin.readline

n = int(input())
perm = [0] + list(map(int, input().split()))

ans = [0] * (n + 1)
for i in range(1, n + 1):
    p_i = perm[i]
    ans[p_i] = i

print(*ans[1:])
