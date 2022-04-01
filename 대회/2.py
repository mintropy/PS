"""
Title : Binary Game 2
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    ans = ''
    for i in range(N + 1):
        ans += str(bin(i))[2:]
    print(ans)
