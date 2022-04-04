"""
Title : 방 번호
Link : https://www.acmicpc.net/problem/1082
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    dp = [[[0, 0] for _ in range(N)] for _ in range(M // min(numbers))]
    ans = 0
    for i in range(M // min(numbers)):
        for j in range(N):
            price_now = numbers[j]
            max_num, price = 0, 0
            for num, p in dp[i - 1]:
                if price_now + p <= M:
                    max_num = num * 10 + j
                    price = price_now + p
            dp[i][j] = [max_num, price]
            if ans < max_num:
                ans = max_num
    print(ans)
