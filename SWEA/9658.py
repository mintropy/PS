'''
Title : 유효숫자 표기
'''
# 파이썬 제출이 없음

t = int(input())
for i in range(t):
    n = str(input())
    if n[0:3] == '999':
        print('#{} {}.{}*10^{}'.format(i + 1, 1, 0, len(n)))
    elif int(n[2]) >= 5 and int(n[1]) == 9:
        print('#{} {}.{}*10^{}'.format(i + 1, int(n[0]) + 1, 0, len(n) - 1))
    elif int(n[2]) >= 5:
        print('#{} {}.{}*10^{}'.format(i + 1, int(n[0]), int(n[1]) + 1, len(n) - 1))
    else:
        print('#{} {}.{}*10^{}'.format(i + 1, int(n[0]), int(n[1]), len(n) - 1))
