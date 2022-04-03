import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().splti())
lunchbox = list(list(map(int, input().split())) for _ in range(n))

lunchbox.sort()
