import sys
input = sys.stdin.readline


n, h, k = map(int, input().split())
locations = [tuple(map(int, input().split())) for _ in range(n)]

