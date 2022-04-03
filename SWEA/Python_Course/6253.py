'''
Title : 흐름과 제어 - 반복 13
'''

n = int(input())
binary = []
while n > 0:
    if n % 2 == 0:
        binary.append(0)
    else:
        binary.append(1)
    n //= 2

for i in range(len(binary)):
    if i == len(binary) - 1:
        print(binary[0])
    else:
        print(binary[-1 -i], end = '')