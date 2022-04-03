'''
Title : 흐름과 제어 - If 1
'''

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print('{}(은)는 {}의 약수입니다.'.format(i, n))