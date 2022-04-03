"""
Title : 비슷한 단어
Link : https://www.acmicpc.net/problem/2607
"""

import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()
word_alphabet = {chr(65 + i):0 for i in range(26)}

for alp in word:
    word_alphabet[alp] += 1

count = 0
for _ in range(n - 1):
    w = input().strip()
    w_alphabet = {chr(65 + i):0 for i in range(26)}
    for alp in w:
        w_alphabet[alp] += 1
    diff = sum([abs(word_alphabet[chr(65 + i)] - w_alphabet[chr(65 + i)]) for i in range(26)])
    if len(word) == len(w) and diff <= 2:
        count += 1
    elif diff <= 1:
        count += 1

print(count)
