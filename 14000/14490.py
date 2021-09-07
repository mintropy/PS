"""
Title : 백대열
Link : https://www.acmicpc.net/problem/14490
"""

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


n, m = map(int, input().split(':'))
g = gcd(n, m)
print(f'{n//g}:{m//g}')
