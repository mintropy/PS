'''
Title : 문자열 1
'''

def is_palindrome(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-1 -i]:
            return False
    return True

s = str(input())
print(s)
if is_palindrome(s):
    print('입력하신 단어는 회문(Palindrome)입니다.')