"""
Title : 사탕상자
Link : https://www.acmicpc.net/problem/2243
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            b = cmd[1]
        elif cmd[0] == 2:
            b, c = cmd[1], cmd[2]

"""
사탕의 맛 1 ~ 1,000,000
    1 맛있는
말 잘들었을 때 맛잇는 사탕, 조금 들어 있을 때 여선 번 째 맛있는 사탕
"""
