"""
Title : 과제 안 내신 분..?
Link : https://www.acmicpc.net/problem/5597
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    students = [False] * 31
    students[0] = True
    for _ in range(28):
        students[int(input().strip())] = True
    for i in range(1, 31):
        if not students[i]:
            print(i)
