'''
Title : 흐름과 제어 - 반복 9
'''

i = 4
while i > 0:
    print(' ' * (4 - i), '*' * (i * 2 - 1), ' ' * (4 - i), sep = '')
    i -= 1