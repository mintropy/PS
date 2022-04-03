'''
Title : 문자열 2
'''

s = list(map(str, input().split()))
for i in range(len(s) - 1):
    print(s[-1 - i], end = ' ')
print(s[0])