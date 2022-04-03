import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())

balls = [a, 0]

if b >= c * d:
    print(-1)
else:
    if a % (c * d - b) == 0:
        print(a // (c * d - b))
    else:
        print(int(a // (c * d - b)) + 1)
        