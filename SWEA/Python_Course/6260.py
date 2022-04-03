'''
Title : 셋, 딕셔너리 8
'''

upper = 0
lower = 0

s = str(input())
for i in range(len(s)):
    if s[i].isupper():
        upper += 1
    elif s[i].islower():
        lower += 1

print(f'UPPER CASE {upper}')
print(f'LOWER CASE {lower}')