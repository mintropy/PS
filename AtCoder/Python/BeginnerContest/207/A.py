import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
print(max(a + b, b + c, c + a))