'''
Title : 흐름과 제어 - If 8
'''

def check(n):
    for i in range(3):
        if int(str(n)[i]) % 2 != 0:
            return False
    return True

print(200, end = '')
for i in range(201, 301):
    if check(i):
        print(',{}'.format(i), end = '')