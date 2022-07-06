"""
Title : A와 B 2
Link : https://www.acmicpc.net/problem/12919
"""

from sys import stdin

input = stdin.readline


def get_reverse_str(s: str) -> str:
    s = s[::-1]
    return s


if __name__ == "__main__":
    S = input().strip()
    T = input().strip()
    word_set = set()
    stack = [T]
    ans = 0
    while stack:
        t = stack.pop()
        if t in word_set:
            continue
        word_set.add(t)
        if t == S:
            ans = 1
            break
        if len(t) <= len(S):
            continue
        if t[-1] == "A":
            stack.append(t[:-1])
        if t[0] == "B":
            stack.append(get_reverse_str(t[1:]))
    print(ans)
