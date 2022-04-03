'''
Title : 이상한 피라미드 탐험
'''

def solution(i: int):
    global first_triangle
    a, b = map(int, input().split())
    # a, b가 위에서부터 몇 번째 줄에 있는지
    for j in range(len(first_triangle) - 1):
        if first_triangle[j] <= a < first_triangle[j + 1]:
            a1 = j
        if first_triangle[j] <= b < first_triangle[j + 1]:
            b1 = j
    if a1 > b1:
        a, b = b, a
        a1, b1 = b1, a1
    a_count_l, a_count_r = a - first_triangle[a1], first_triangle[a1 + 1] - 1 - a
    b_count_l, b_count_r = b - first_triangle[b1], first_triangle[b1 + 1] - 1 - b
    if a1 == b1:
        ans = abs(b - a)
    elif a_count_l <= b_count_l and a_count_r <= b_count_r:
        ans = b1 - a1
    else:
        ans = b1 - a1
        ans += min(abs(b_count_r - a_count_r), abs(b_count_l - a_count_l))
        '''
        if b_count_l < b_count_r:
            ans += abs(b_count_r - a_count_r)
        else:
            ans += abs(b_count_l - a_count_l)
        '''
    print('#', i, ' ', ans, sep = '')


t = int(input())
first_triangle = []
a, b = 1, 1
while True:
    first_triangle.append(a)
    if a > 10000:
        break
    a += b
    b += 1

for i in range(t):
    solution(i + 1)