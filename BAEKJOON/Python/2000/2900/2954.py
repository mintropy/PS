"""
Title : Brainf**k 인터프리터
Link : https://www.acmicpc.net/problem/3954
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        sm, sc, si = map(int, input().split())
        program = input().strip()
        program_input = input().strip()
