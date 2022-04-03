'''
Title : IOIOI
Link : https://www.acmicpc.net/problem/5525
'''

import sys

input = sys.stdin.readline
# 찾는 문자열 P 길이, 문자열 S 길이
n, m = int(input()), int(input())
s = str(input().strip())
# 문자열 s에서 p문자열의 시작, 끝을 나타내는 인덱스
st, end = -1, -1
# 지금 보고 있는 인덱스
idx = 0
# 찾은 문자열 개수
count = 0

for i in range(m - (2 * n) - 1):
    if s[i] == 'I':
        if s[i + 1:i + 2 * n + 1] == 'OI' * n:
            count += 1

print(count)