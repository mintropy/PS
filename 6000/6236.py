"""
Title : 용돈 관리
Link : https://www.acmicpc.net/problem/6236
"""

import sys
input = sys.stdin.readline


def bin_search(m: int, money: list) -> int:
    st, end = 0, sum(money)
    ans = sum(money)
    while st <= end:
        mid = (st + end) // 2
        # 출금 횟수
        withdraw = count_withdraw(money, mid)
        if withdraw >= m:
            if mid < ans and withdraw != 10 ** 6:
                ans = mid
            st = mid + 1
        else:
            end = mid - 1
    return ans


def count_withdraw(money: list, mid: int) -> int:
    withdraw = 1
    money_now = mid
    for m in money:
        if m > money_now:
            withdraw += 1
            if m > mid:
                return 10 ** 6
            money_now = mid - m
        else:
            money_now -= m
    return withdraw



n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))

print(bin_search(m, money))
