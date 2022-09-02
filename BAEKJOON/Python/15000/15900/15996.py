"""
Title : 팩토리얼 나누기
Link : https://www.acmicpc.net/problem/15996
"""

n, a = map(int, input().split())
power = [a]
while True:
    if power[-1] > n:
        power.pop()
        break
    else:
        power.append(power[-1] * a)

if len(power) == 1:
    print(n // a)
else:
    count = 0
    for p in power:
        count += n // p
    
    print(count)
