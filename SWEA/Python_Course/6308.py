'''
Title : 내장함수 1
'''

import time
y = time.time()
y = time.strftime('%Y')
y = int(y)

name = str(input())
age = int(input())

print('{}(은)는 {}년에 100세가 될 것입니다.'.format(name, y + 100 - age))