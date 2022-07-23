import sys

input = sys.stdin.readline

n, a, x, y = map(int, input().split())

if n <= a:
    print(n * x)
elif n > a:
    print(a * x + (n - a) * y)