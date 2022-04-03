'''
Title : 함수의 기초 2
'''

def solution():
    _ = str(input())
    _ = str(input())
    s1 = str(input())
    s2 = str(input())
    if (s1 == '가위' and s2 == '바위') or (s1 == '바위' and s2 == '보') or (s1 == '보' and s2 == '가위'):
        print(s2, '가 이겼습니다!', sep = '')
    else:
        print(s1, '가 이겼습니다!', sep = '')

solution()