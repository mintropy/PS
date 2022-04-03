import sys
input = sys.stdin.readline

n = int(input())

idx = 0
m = 1
while True:
    if m > n:
        print(idx - 1)
        break
    else:
        idx += 1
        m *= 2
