'''
Title : 셋, 딕셔너리 7
'''

s = str(input())
letters = 0
digits = 0

for i in range(len(s)):
    if s[i].isalpha():
        letters += 1
    elif s[i].isdigit():
        digits += 1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')