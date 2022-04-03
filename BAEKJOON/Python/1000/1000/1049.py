"""
Title : 기타줄
Link : https://www.acmicpc.net/problem/1049
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
min_package_price = min_line_price = 1000

for _ in range(M):
    pcg, li = MIIS()
    if min_package_price > pcg:
        min_package_price = pcg
    if min_line_price > li:
        min_line_price = li


if min_package_price > min_line_price * 6:
    print(min_line_price * N)
else:
    total_price = min_package_price * (N // 6)
    N %= 6
    if min_package_price > N * min_line_price:
        print(total_price + N * min_line_price)
    else:
        print(total_price + min_package_price)
