'''
Title : 자료구조 - 리스트, 튜플 17
'''

import math

num = list(map(int, input().split(',')))

ans = []
for x in num:
    ans.append(round(2 * x * math.pi, 2))

for i in range(3):
    print(ans[i], ', ', sep = '', end = '')
print(ans[-1])