'''
Title : 십자카드 문제
Link : https://www.acmicpc.net/problem/2659
'''

import sys

# 가장 작은 시계수 찾기 함수
def find_clock_num(num: list) -> int:
    tmp = []
    tmp.append(num[0] * 1000 + num[1] * 100 + num[2] * 10 + num[3])
    tmp.append(num[1] * 1000 + num[2] * 100 + num[3] * 10 + num[0])
    tmp.append(num[2] * 1000 + num[3] * 100 + num[0] * 10 + num[1])
    tmp.append(num[3] * 1000 + num[0] * 100 + num[1] * 10 + num[2])
    return min(tmp)

clock_num = [False] * 10000
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                n = find_clock_num([i, j, k, l])
                if not clock_num[n]:
                    clock_num[n] = True
        
num = list(map(int, input().split()))
target = find_clock_num(num)
count = 0
for i in range(1111, target + 1):
    if clock_num[i]:
        count += 1
print(count)
