"""
Title : 용돈 관리
Link : https://www.acmicpc.net/problem/6236
"""

import sys
input = sys.stdin.readline


def bin_search(m: int, money: list) -> int:
    st, end = max(money), sum(money)
    ans = sum(money)
    while st <= end:
        mid = (st + end) // 2
        # m번 출금 가능할 때, 더 작은 금액 가능한지 확인
        if count_withdraw(m, money, mid):
            if mid < ans:
                ans = mid
            end = mid - 1
        else:
            st = mid + 1
    return ans


# m번 인출이 가능한지 확인
def count_withdraw(withdraw_count: int, money: list, mid: int) -> int:
    # 0번에서 확인해가는 대신, 모든 날 인출하는 것에서 줄일 수 있는지 확인
    withdraw = len(money)
    money_now = mid
    money_for_day_count = 0
    for m in money:
        if m > money_now:
            withdraw -= money_for_day_count - 1
            # 출금 제한 횟수보다 더 적게 가능하면 True
            # 압축한 날을 뽑아 둘로 나누는 작업하면 개수 맞출 수 있음
            if withdraw <= withdraw_count:
                return True
            money_for_day_count = 1
            money_now = mid - m
        else:
            money_for_day_count += 1
            money_now -= m
    # 마지막 날까지 탐색하고 한번 더 확인
    withdraw -= money_for_day_count - 1
    if withdraw <= withdraw_count:
        return True
    else:
        return False


n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))

print(bin_search(m, money))


'''
Counter Example
5 3
100
100
100
100
100
ans : 200
output : 100


5 2
100
100
100
100
100
ans : 300
output : 400
'''