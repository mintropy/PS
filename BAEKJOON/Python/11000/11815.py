"""
Title : 짝수? 홀수?
Link : https://www.acmicpc.net/problem/11815
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    ans = ""
    for x in nums:
        if x == int(x**0.5) ** 2:
            ans += "1 "
        else:
            ans += "0 "
    print(ans)
