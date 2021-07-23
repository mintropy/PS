'''
Title : 책 페이지
Link : https://www.acmicpc.net/problem/1019
'''

import sys

n = int(sys.stdin.readline())
digits = [0]
while True:
    x = n % 10
    n //= 10
    digits.append(x)
    if n == 0:
        break

# 숫자별 사용된 개수
num = [0] * 10
base = [1] * 10

# i자리 수에서 각 수가 나오는 개수 (1 ~ 9)
num_count = [0] * 10
num_count[1] = 1
for i in range(2, 10):
    num_count[i] = 10 ** (i - 1) + num_count[i - 1] * 9

# 0부터 9까지 나오는 개수 확인
for i in range(1, len(digits)):
    n_th_digit = digits[i]
    count = 0
    if i == len(digits) - 1:
        target = 0
        for k in range(i):
            if k == i - 1:
                target += 9 * (10 ** k) * (i - 1) * (n_th_digit - 1) + 1
            else:
                target += 9 * (10 ** k) * i
    else:
        target = n_th_digit * (10 ** (i - 1)) * i
    for j in range(1, 10):
        if j > n_th_digit:
            num[j] += n_th_digit * num_count[i - 1]
        elif j == n_th_digit:
            num[j] += 1 + n_th_digit * num_count[i - 1]
            count += 1 + n_th_digit * num_count[i - 1]
        elif j < n_th_digit:
            num[j] += 10 ** (i - 1) + num_count[i - 1]
            count += 10 ** (i - 1) + num_count[i - 1]
    num[0] += target - count

for x in num:
    print(x, end = ' ')