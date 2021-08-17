"""
Title : 파닭파닭
Link : https://www.acmicpc.net/problem/14627
"""

import sys
input = sys.stdin.readline


def bin_search(c, spring_onion) -> int:
    st, end = 0, sum(spring_onion) // 2
    # 파닭에 넣을 가장 긴 파의 길이
    ans = 0
    while st <= end:
        mid = (st + end) // 2
        if mid == 0:
            so_count = 0
        else:
            so_count = sum([i // mid for i in spring_onion])
        if so_count >= c:
            if mid >= ans:
                ans = mid
            st = mid + 1
        else:
            end = mid - 1
    return ans


s, c = map(int, input().split())

spring_onion = [int(input()) for _ in range(s)]

so_lenght = bin_search(c, spring_onion)

if s == 1:
    so_lenght = spring_onion[0] // c
    print(spring_onion[0] - so_lenght * c)
elif so_lenght == 0:
    print(sum(spring_onion))
else:
    so_count = sum([i // so_lenght for i in spring_onion])
    so_lenght_left = sum([i % so_lenght for i in spring_onion])

    print(so_lenght_left + (so_count - c) * so_lenght)


'''
counter example
1 3
3
ans : 0
output = 3
'''