"""
Title : 화성 수학
Link : https://www.acmicpc.net/problem/5355
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        n, *cmd = input().strip().split()
        n = float(n)
        for x in cmd:
            if x == "@":
                n *= 3
            elif x == "%":
                n += 5
            elif x == "#":
                n -= 7
        print("{:.2f}".format(n))
