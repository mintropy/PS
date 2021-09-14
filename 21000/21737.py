"""
Title : SMUPC 계산기
Link : https://www.acmicpc.net/problem/21737
"""

import sys
input = sys.stdin.readline


def operate(num1: int, num2: int, operation: str) -> int:
    if operation_last == 'S':
        return num1 - num2
    elif operation_last == 'M':
        return num1 * num2
    elif operation_last == 'U':
        if num1 >= 0:
            return num1 // num2
        else:
            num1 *= -1
            num1 //= num2
            return num1 * -1
    elif operation_last == 'P':
        return num1 + num2


n = int(input())
poly = input().strip()

idx = 0
num_last = 0
operation_last = ''
num_now = 0
# num_now에 입력하고 있는지, 새로 입력해야 하는지
new_num = False
output = []

while idx < len(poly):
    if poly[idx].isalpha():
        # c이면 output에 저장
        if poly[idx] == 'C':
            if operation_last:
                num_now = operate(num_last, num_now, operation_last)
                new_num = False
                output.append(num_now)
                operation_last = ''
            else:
                output.append(num_now)
        # 처음 연산자를 만났을 때
        elif operation_last == '':
            num_last = num_now
            operation_last = poly[idx]
            num_now = 0
        # 아니라면 이전 연산을 하고, 연산자 새로 추가
        else:
            num_now = operate(num_last, num_now, operation_last)
            new_num = False
            operation_last = poly[idx]
    # 숫자일 때
    else:
        if new_num:
            num_now *= 10
            num_now += int(poly[idx])
        else:
            new_num = True
            num_last = num_now
            num_now = int(poly[idx])
    idx += 1

if output:
    print(*output)
else:
    print('NO OUTPUT')
