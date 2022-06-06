"""
Title : 팰린드롬 만들기
Link : https://www.acmicpc.net/problem/1213
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    s = input().strip()
    l = len(s)
    alpahbets = [0] * 26
    for x in s:
        alpahbets[ord(x) - 65] += 1

    odd_count = 0
    for y in alpahbets:
        if y % 2:
            odd_count += 1

    if odd_count >= 2 or (not l % 2 and odd_count == 1):
        print("I'm Sorry Hansoo")
    else:
        ans = [""] * len(s)
        idx = 0
        for x, count in enumerate(alpahbets):
            if count % 2:
                ans[l // 2] = chr(x + 65)
            for _ in range(count // 2):
                ans[idx] = ans[-1 - idx] = chr(x + 65)
                idx += 1
        print("".join(ans))
