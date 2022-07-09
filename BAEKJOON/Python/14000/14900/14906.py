"""
Title : 스러피
Link : https://www.acmicpc.net/problem/14906
"""

import re
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    print("SLURPYS OUTPUT")
    for _ in range(int(input())):
        s = input().strip()
        if s == "AH" or s:
            print("YES")
        else:
            print("NO")
    print("END OF OUTPUT")
