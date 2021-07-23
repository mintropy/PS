'''
Title : 이진수 변환
Link : https://www.acmicpc.net/problem/10829
'''

import sys

input = sys.stdin.readline

n = int(input())

binary = ''

while n > 0:
    if n % 2 == 0:
        binary = '0' + binary
    else:
        binary = '1' + binary
    n //= 2

print(int(binary))