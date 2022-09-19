"""
Title : 단어 섞기
Link : https://www.acmicpc.net/problem/9177
"""

from collections import deque
from sys import stdin

input = stdin.readline


def search(s1: str, s2: str, s3: str) -> str:
    len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
    check = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x + y == len_s3:
            return "yes"
        if check[x][y]:
            continue
        check[x][y] = True
        if x < len_s1 and s1[x] == s3[x + y]:
            queue.append((x + 1, y))
        if y < len_s2 and s2[y] == s3[x + y]:
            queue.append((x, y + 1))
    return "no"


if __name__ == "__main__":
    ans = ""
    for i in range(int(input())):
        s1, s2, s3 = input().strip().split()
        ans += f"Data set {i + 1}: {search(s1, s2, s3)}\n"
    print(ans)
