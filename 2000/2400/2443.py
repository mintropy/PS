"""
Title : 별 직기 - 6
Link : https://www.acmicpc.net/problem/2443
"""

n = int(input())

for i in range(n):
    print(' ' * i + '*' * ((n - i) * 2 - 1))