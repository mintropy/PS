"""
Title : 소음
Link : https://www.acmicpc.net/problem/2935
"""

from sys import stdin

input = stdin.readline
IS = lambda: input().strip()

if __name__ == "__main__":
    ans = eval("".join([IS() for _ in range(3)]))
    print(ans)
