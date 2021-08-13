"""
Title : 조화평균
Link : https://www.acmicpc.net/problem/2090
"""


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_lcd(a, b, g):
    a1 = a // g
    b1 = b // g
    return a1 * b1 * g


n = int(input())
seq = list(map(int, input().split()))


if n == 1:
    print(f'{seq[0]}/1')
else:
    gcd = find_gcd(seq[0], seq[1])
    lcd = find_lcd(seq[0], seq[1], gcd)
    for i in range(2, n):
        gcd = find_gcd(seq[i], lcd)
        lcd = find_lcd(seq[i], lcd, gcd)
    
    numerator = 0
    for num in seq:
        numerator += lcd // num
    
    # 약분 가능한지
    gcd = find_gcd(lcd, numerator)
    lcd //= gcd
    numerator //= gcd
    
    print(f'{lcd}/{numerator}')
