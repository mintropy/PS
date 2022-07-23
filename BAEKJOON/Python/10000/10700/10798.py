"""
Title : 세로읽기
Link : https://www.acmicpc.net/problem/10798
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    seq = [input().strip() for _ in range(5)]
    ans = ""
    for j in range(15):
        for i in range(5):
            if len(seq[i]) < j + 1:
                continue
            ans += seq[i][j]
    print(ans)
