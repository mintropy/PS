import sys
input = sys.stdin.readline


N, K, A = map(int, input().split())

K %= N

if K:
    A += (K - 1)
    if A > N:
        A -= N
else:
    A -= 1
    if A == 0:
        A = N

print(A)
