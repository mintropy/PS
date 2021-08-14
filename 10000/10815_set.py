"""
Title :  숫자 카드
Link : https://www.acmicpc.net/problem/10815
"""

import sys
input = sys.stdin.readline
    

n = int(input())
card = set(map(int, input().split()))
m = int(input())
ans = ''
for k in map(int, input().split()):
    if k in card:
        # print(1, end = ' ')
        ans += '1 '
    else:
        # print(0, end = ' ')
        ans += '0 '
print(ans)


'''
# map 없이
# 시간 비슷함
n = int(input())
card = set(input().split())
m = int(input())
for k in input().split():
    if k in card:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
'''