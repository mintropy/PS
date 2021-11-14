"""
Title : 토달기
Link : https://www.acmicpc.net/problem/1897
"""

import sys
input = sys.stdin.readline


d, string_0 = input().strip().split()
additional_strings = {}
for _ in range(int(d)):
    string = input().strip()
    if len(string) in additional_strings:
        additional_strings[len(string)].append(string)
    else:
        additional_strings[len(string)] = [string]



