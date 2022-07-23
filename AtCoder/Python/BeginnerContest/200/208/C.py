import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ID = list(map(int, input().split()))
count = [0] * n

if k > n:
    r = k // n
    k -= r * n
    for i in range(n):
        count[i] += r
if k > 0:
    idx = ID.index(min(ID))
    count[idx] += k

for x in count:
    print(x)