"""
Title : 별 찍기 - 11
Link : https://www.acmicpc.net/problem/2448
"""

import sys

input = sys.stdin.readline


n = int(input())
stars = ['  *  ', ' * * ', '*****']
count = 3

while n > 3:
    new_stars = []
    # 위쪽 자기 모양
    for star in stars:
        new_stars.append(' ' * count + star + ' ' * count)
    # 아래쪽 자기 모양 * 2
    for star in stars:
        new_stars.append(star + ' ' + star)

    n //= 2
    count *= 2
    stars = new_stars

for star in stars:
    print(star)