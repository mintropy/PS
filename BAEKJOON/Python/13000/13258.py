"""
Title : 복권 + 은행
Link : https://www.acmicpc.net/problem/13258
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


def calc_next(now: float, win_prob: float, prize: int) -> float:
    win_money = now + prize
    return win_money * win_prob + now * (1 - win_prob)


if __name__ == "__main__":
    N = II()
    accounts = list(map(int, input().split()))
    J = II()
    C = II()
    for _ in range(C):
        total_accounts = sum(accounts)
        accounts = [calc_next(now, now / total_accounts, J) for now in accounts]
    print(accounts[0])
