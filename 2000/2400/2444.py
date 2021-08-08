"""
Title : 별 찍기 -7
Link : https://www.acmicpc.net/problem/2444
"""

n = int(input())

for i in range(n - 1, 0, -1):
    print(' ' * i + '*' *((n - i) * 2 - 1))
print('*' * (n * 2 -1))
for i in range(1, n):
    print(' ' * i + '*' *((n - i) * 2 - 1))