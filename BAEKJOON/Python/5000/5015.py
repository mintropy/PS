"""
title : ls
Link : https://www.acmicpc.net/problem/5015
"""

import re
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    P = input().strip()
    length = len(P)
    for _ in range(int(input())):
        file_name = input().strip()
        idx = 0
