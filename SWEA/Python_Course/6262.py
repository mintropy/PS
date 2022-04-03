'''
Title : 셋, 딕셔너리 8
'''

s = str(input())
d = {}

for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

for key in sorted(d.keys()):
    print(f'{key},{d[key]}')