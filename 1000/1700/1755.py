"""
Title : 숫자놀이
Link : https://www.acmicpc.net/problem/1755
"""

import sys
input = sys.stdin.readline


M, N = map(int, input().split())

num_to_eng = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}
eng_to_num = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

nums = []
for num in range(M, N + 1):
    tmp = []
    while num:
        tmp.append(num_to_eng[num % 10])
        num //= 10
    if len(tmp) == 2:
        nums.append(' '.join(tmp[::-1]))
    else:
        nums.append(tmp[0])

nums.sort()
tmp = []
for num in nums:
    new_num = 0
    num = list(num.split())
    for n in num:
        new_num *= 10
        new_num += eng_to_num[n]
    tmp.append(new_num)
    if len(tmp) == 10:
        print(*tmp)
        tmp = []
if tmp:
    print(*tmp)
