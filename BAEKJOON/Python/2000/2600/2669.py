"""
Title : 직사각형 네개의 합집합의 면적 구하기
Link : https://www.acmicpc.net/problem/2669
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    plain = [[False] * 101 for _ in range(101)]
    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                plain[i][j] = True
    ans = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if plain[i][j]:
                ans += 1
    print(ans)
