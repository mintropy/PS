import sys
input = sys.stdin.readline

s, t = input().strip().split()

if s < t:
    print('Yes')
else:
    print('No')
