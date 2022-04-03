import sys
input = sys.stdin.readline


x = int(input())

if x == 0 or x % 100:
    print('No')
else:
    print('Yes')