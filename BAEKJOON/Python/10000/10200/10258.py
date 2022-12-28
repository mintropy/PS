"""
Title : 스위치 배열
Link : https://www.acmicpc.net/problem/10258
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    toggle_1_0 = [0, 1, 2]
    toggle_10_00 = [0, 1]
    for _ in range(30):
        toggle_10_00.append(toggle_10_00[-1] * 2 + 1)
    for i in range(3, 29):
        toggle_1_0.append(toggle_1_0[-2] + 1 + toggle_10_00[i - 1])

    for _ in range(int(input())):
        B = list(int(x) for x in input().strip())
        toggle = 0
        
