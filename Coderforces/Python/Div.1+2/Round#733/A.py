import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = str(input().strip())
    max_digit = 0
    for i in range(len(n)):
        if int(n[i]) > max_digit:
            max_digit = int(n[i])
    print(max_digit)