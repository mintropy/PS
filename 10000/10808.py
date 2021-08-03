"""
Title : 알파벳 개수
Link : https://www.acmicpc.net/problem/10808
"""

s = list(input())
check = [0] * 26

for alph in s:
    check[ord(alph) - ord('a')] += 1

print(*check)