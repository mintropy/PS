'''
Title : 흐름과 제어 - If 4
'''

s1 = str(input())
s2 = str(input())


if s1 == s2:
    print('Result : Draw')
elif (s1 == '가위' and s2 == '보') or (s1 == '바위' and s2 == '가위') or (s1 == '보' and s2 == '바위'):
    print('Result : Man1 Win!')
else:
    print('Result : Man2 Win!')