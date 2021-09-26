"""
Title : 참가자 명단
Link : https://www.acmicpc.net/problem/23056
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

student = {f'{i}':[] for i in range(1, n + 1)}
while True:
    c, st = input().strip().split()
    if c == '0' and st == '0':
        break
    student[c].append(st)

# 홀수 반
for i in range(1, n + 1, 2):
    applicated = student[f'{i}']
    if len(applicated) >= m:
        applicated = applicated[:m]
    applicated.sort(key=lambda x:[len(x), x])
    for applicant in applicated:
        print(i, applicant)
# 짝수 반
for i in range(2, n + 1, 2):
    applicated = student[f'{i}']
    if len(applicated) >= m:
        applicated = applicated[:m]
    applicated.sort(key=lambda x:[len(x), x])
    for applicant in applicated:
        print(i, applicant)


'''
counter example
2 4
0 0
'''