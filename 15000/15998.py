"""
Title : 카카오머니
Link : https://www.acmicpc.net/problem/15998
"""

from math import gcd
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    balance = 0
    max_in = -1
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        money = b - a - balance
        if money > 0:
            ans = gcd(ans, money)
            max_in = max(max_in, b)
        elif money < 0:
            print(-1)
            break
        balance = b
    if ans > max_in:
        print(ans if ans else 1)
    else:
        print(-1)

'''
2
-5 0
-6 0
# 1

2
1500 1500
-300 1200
# 1

3
1500 1500
-1600 1200
-400 0
# -1

'''
