"""
Title : 비트코인은 신이고 나는 무적이다
Link : https://www.acmicpc.net/problem/23257
"""

# https://stackoverflow.com/questions/52108901/xor-operation-on-three-values

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def multiple_XOR(values: list):
    value_now = values[0] ^ values[1]
    for i in range(1, len(values) - 1):
        value_now |= values[i] ^ values[i + 1]
    return value_now


n, m = MIIS()
montly_bong = list(MIIS())
for i in range(n):
    montly_bong[i] = abs(montly_bong[i])

dp = [[montly_bong[i]] for i in range(n)]
# 2개에서 n개 선택
for _ in range(2, m + 1):
    for i in range(n):
        price_list_next = []
        price_list_now = dp[i][::]
        price_next = -1
        for j in range(i + 1):
            price_list_now.append(montly_bong[j])
            xor_value = multiple_XOR(price_list_now)
            if xor_value >= price_next:
                price_next = xor_value
                price_list_next = price_list_now[::]
            price_list_now.pop()
        dp[i] = price_list_next[::]

if m == 1:
    print(max(montly_bong))
else:
    print(max([multiple_XOR(dp[i]) for i in range(n)]))
