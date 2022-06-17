"""
Title : 명령 프롬프트
Link  : https://www.acmicpc.net/problem/1032
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    commands = list(input().strip() for _ in range(N))
    cmd_length = len(commands[0])
    ans = []
    for j in range(cmd_length):
        char = commands[0][j]
        for i in range(1, N):
            if commands[i][j] != char:
                ans.append("?")
                break
        else:
            ans.append(char)
    print("".join(ans))
