'''
Title : 흐름과 제어 - If 6
'''

s = str(input())

if s == s.lower():
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(s, ord(s), s.upper(), ord(s.upper())))
else:
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(s, ord(s), s.lower(), ord(s.lower())))