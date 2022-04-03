'''
Title : 함수의 기초 9
'''

def solution():
    s1, s2 = map(str, input().split(','))
    s2 = s2[1:]
    if len(s1) > len(s2):
        print(s1)
    else:
        print(s2)
    
solution()