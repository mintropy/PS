"""
Title : 로마숫자
Link : https://www.acmicpc.net/problem/13273
"""

import re
from sys import stdin

input = stdin.readline


def arabic_to_rome(arabic: str) -> str:
    res = ""
    l = len(arabic)
    for idx, x in enumerate(arabic):
        if x == "4":
            if l - idx == 3:
                res += "CD"
            elif l - idx == 2:
                res += "XL"
            elif l - idx == 1:
                res += "IV"
        elif x == "9":
            if l - idx == 3:
                res += "CM"
            elif l - idx == 2:
                res += "XC"
            elif l - idx == 1:
                res += "IX"
        else:
            x = int(x)
            if 5 <= x <= 8:
                if l - idx == 3:
                    res += "D"
                elif l - idx == 2:
                    res += "L"
                elif l - idx == 1:
                    res += "V"
                x -= 5
            if idx == 0:
                res += "M" * x
            elif idx == 1:
                res += "C" * x
            elif idx == 2:
                res += "X" * x
            elif idx == 3:
                res += "I" * x
    return res


def rome_to_arabic(rome: str) -> str:
    res = []
    idx = 0
    l = len(rome)
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        num = input().strip()
        match = re.match("[0-9]*", num)
        if match.group(0) == num:
            print(arabic_to_rome(num))
        else:
            print(rome_to_arabic[num])
