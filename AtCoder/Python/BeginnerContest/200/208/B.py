import sys

input = sys.stdin.readline

p = int(input())

factorial = [0, 1]
for i in range(2, 11):
    factorial.append(factorial[-1] * i)

count = 0
for i in range(10, 0, -1):
    if factorial[i] <= p:
        c = p // factorial[i]
        count += c
        p -= factorial[i] * c

print(count)