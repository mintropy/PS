import sys

input = sys.stdin.readline

n = int(input())
n = int(n * 1.08)

if n < 206:
    print('Yay!')
elif n == 206:
    print('so-so')
elif n > 206:
    print(':(')