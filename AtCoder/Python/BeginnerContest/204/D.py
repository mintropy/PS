import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]
