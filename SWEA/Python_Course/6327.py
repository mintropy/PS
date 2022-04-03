'''
Title : 함수의 기초 8
'''

a, b = map(int, input().split(','))
def sqr(a, b):
    print('square({}) => {}'.format(a, a ** 2))
    print('square({}) => {}'.format(b, b ** 2))
sqr(a, b)