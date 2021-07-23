'''
Title : 영화감독 숌
Link : https://www.acmicpc.net/problem/1436
'''

import sys

input = sys.stdin.readline

n = int(input())
num = '666'
now = 666
count = 0

while True:
    if num in str(now):
        count += 1
    if count == n:
        print(now)
        break
    now += 1

