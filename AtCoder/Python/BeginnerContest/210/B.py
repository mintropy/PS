import sys

input = sys.stdin.readline

n = int(input())
s = str(input())

for i in range(n):
    if s[i] == '1':
        if i % 2 == 0:
            print('Takahashi')
            break
        elif i % 2 == 1:
            print('Aoki')
            break