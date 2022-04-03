'''
Title : 자릿수 더하기
'''

n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)