"""
Title : 팰린드롬 만들기
Link : https://www.acmicpc.net/problem/1254
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    s = input().strip()
    l = len(s)
    if s == s[::-1]:
        print(l)
        exit()
    if l == 1:
        print(1)
        exit()
    if l == 2:
        if s[0] == s[1]:
            print(2)
        else:
            print(3)
        exit()

    for mid in range(l // 2 + l % 2, l):
        if s[mid] == s[mid - 1]:
            for i in range(l - mid - 1):
                if s[mid + i + 1] != s[mid - i - 2]:
                    break
            else:
                print(l + mid * 2 - l)
                break
        for i in range(l - mid - 1):
            if s[mid + i + 1] != s[mid - i - 1]:
                break
        else:
            print(l + mid * 2 - l + 1)
            break


"""
Counter Example

eqqee
out : 4
ans : 8
"""
