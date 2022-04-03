'''
Title : 흐름과 제어 - 반복 10
'''

num = [0] * 10
n = str(input())

for i in range(len(n)):
    num[int(n[i])] += 1

for i in range(10):
    if i < 9:
        print(i, end = ' ')
    else:
        print(i)
for i in range(10):
    if i < 9:
        print(num[i], end = ' ')
    else:
        print(num[i])