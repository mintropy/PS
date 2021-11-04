"""
Title : 최종 순위
Link : https://www.acmicpc.net/problem/7775
"""

n, p, k, d = map(int, input().split())

if d == 1:
    if n == k:
        if p % k:
            print('Wrong information')
        else:
            grades = [p // k] * k
            print(*grades, sep='\n')
    else:
        grades = [p // k] * k + [p % k] + [0] * (n - k - 1)
elif n == k:
    if p % k:
        print('Wrong information')
    else:
        grades = [p // k] * k
        print(*grades, sep='\n')
else:
    grades = [0] * n
    for i in range(k - d):
        grades[i] = k - d - i
    if sum(grades) > p:
        print('Wrong information')
    elif sum(grades) == p:
        print(*grades, sep='\n')
    else:
        grades[0] += p - sum(grades)
        print(*grades, sep='\n')
