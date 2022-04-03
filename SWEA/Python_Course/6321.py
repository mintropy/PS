'''
Title : 함수의 기초 3
'''

n = int(input())

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print('소수입니다.')
else:
    print('소수가 아닙니다.')