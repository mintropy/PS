'''
Title : 함수의 기초 1
'''

s = str(input())

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 -i]:
            return False
    return True

if is_palindrome(s):
    print(s)
    print('입력하신 단어는 회문(Palindrome)입니다.')