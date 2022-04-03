'''
Title : 흐름과 제어 - If 2
'''

n = int(input())
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)
        print('{}(은)는 {}의 약수입니다.'.format(i, n))
if len(divisor) == 2:
    print('{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.'.format(n, 1, n))