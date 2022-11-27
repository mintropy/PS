"""
Title : 팰린드롬 만들기
Link : https://www.acmicpc.net/problem/1254
"""

from sys import stdin

input = stdin.readline


def solve(s: str) -> int:
    l = len(s)
    if s == s[::-1] or l == 1:
        return l
    for mid in range(l // 2 + l % 2, l):
        if s[mid] == s[mid - 1]:
            for i in range(l - mid - 1):
                if s[mid + i + 1] != s[mid - i - 2]:
                    break
            else:
                return l + mid * 2 - l
        for i in range(l - mid - 1):
            if s[mid + i + 1] != s[mid - i - 1]:
                break
        else:
            return l + mid * 2 - l + 1


if __name__ == "__main__":
    s = input().strip()
    print(solve(s))

"""
Counter Example

eqqee
out : 4
ans : 8
"""
