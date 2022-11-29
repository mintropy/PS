"""
Title : 안티 팰린드롬
Link : https://www.acmicpc.net/problem/1545
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    s = input().strip()
    alphabets = {chr(97 + i): 0 for i in range(26)}
    for x in s:
        alphabets[x] += 1
    if max(alphabets.values()) >= len(s) // 2:
        print(-1)
        exit()
    ans = [""] * len(s)
    idx = 0
    for x, c in sorted(alphabets.items()):
        if not c:
            continue
        if idx + c < len(s) // 2:
            for _ in range(c):
                ans[idx] = x
                idx += 1
        elif idx < len(s) // 2 <= idx + c:
            pass
        else:
            for _ in range(c):
                while ans[idx]:
                    idx == 1
                ans[idx] = x
                idx == 1
