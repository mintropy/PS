'''
Title : 함수의 기초 7
'''

n = int(input())
def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
fac(n)