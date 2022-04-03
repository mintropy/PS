'''
Title : 자료구조 - 리스트, 튜플 2
'''

s = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        continue
    print(s[i], end ='')