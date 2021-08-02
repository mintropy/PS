"""
Title : 별 찍기 - 23
Link : https://www.acmicpc.net/problem/13015
"""

import sys
input = sys.stdin.readline

n = int(input())
stars = []

# *****       ***** : 5일때 공백 7
# 1 + 2 * 3 = 1 + 2 * (5 - 2)

# 첫 줄 추가
stars.append('*' * n + ' ' * ((n - 2) * 2 + 1) + '*' * n)
# 두번째 줄 부터 중간줄 사이
for i in range(1, n - 1):
    line = ''
    line += ' ' * i
    line += '*' + ' ' * (n - 2) + '*'
    line += ' ' * (n - 2 - i)
    line += ' '
    line += ' ' * (n - 2 - i)
    line += '*' + ' ' * (n - 2) + '*'
    stars.append(line)
# 중간 추가
stars.append(' ' * (n - 1) + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')
# 중간부터 밑으로
for i in range(n - 2, 0, -1):
    line = ''
    line += ' ' * i
    line += '*' + ' ' * (n - 2) + '*'
    line += ' ' * (n - 2 - i)
    line += ' '
    line += ' ' * (n - 2 - i)
    line += '*' + ' ' * (n - 2) + '*'
    stars.append(line)
# 마지막 줄
stars.append('*' * n + ' ' * ((n - 2) * 2 + 1) + '*' * n)

for star in stars:
    print(star)