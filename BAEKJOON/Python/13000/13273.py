"""
Title : 로마숫자
Link : https://www.acmicpc.net/problem/13273
"""

import re
from sys import stdin

input = stdin.readline


def make_rome(arabic: str) -> str:
    res = ""
    l = len(arabic)
    for idx, x in enumerate(arabic):
        pass


if __name__ == "__main__":
    for _ in range(int(input())):
        num = input().strip

        match = re.match("[0-9]*", num)
        if match.group(0) == num:

            print(True)
        else:

            print(False)
