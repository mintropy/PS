"""
Title : 접미사 배열
Link : https://www.acmicpc.net/problem/11656
"""

s = input().strip()

suffix = []
for i in range(len(s)):
    suffix.append(s[i:])

print(*sorted(suffix), sep = '\n')