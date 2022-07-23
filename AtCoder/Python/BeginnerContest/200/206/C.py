import sys, collections

input = sys.stdin.readline

n = int(input())
d = collections.defaultdict(int)

array = list(map(int, input().split()))
for x in array:
    d[x] += 1

v = list(d.values())
ans = (n * (n - 1)) // 2
for x in v:
    if x == 1:
        continue
    else:
        ans -= (x * (x - 1)) // 2

print(ans)