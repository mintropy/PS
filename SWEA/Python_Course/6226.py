'''
Title : 흐름과 제어 - If 7
'''

print(7, end = '')
for i in range(8, 201):
    if i % 5 != 0 and i % 7 == 0:
        print(',{}'.format(i), end = '')