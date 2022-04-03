'''
Title : 자료구조 - 리스트, 튜플 6
'''

n = int(input())
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)
print(divisor)