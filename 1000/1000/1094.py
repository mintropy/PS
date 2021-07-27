import sys

input = sys.stdin.readline

n = int(input())

count = 0
while n:
    if n & 1:
        count += 1
    n = n >> 1
print(count)