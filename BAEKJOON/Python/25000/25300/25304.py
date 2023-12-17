"""
Title : 영수증
Link : https://www.acmicpc.net/problem/25304
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    X = int(input())
    total_price = 0
    for _ in range(int(input())):
        price, count = map(int, input().split())
        total_price += price * count
    print("Yes" if total_price == X else "No")
