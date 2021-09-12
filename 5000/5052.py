"""
Title : 전화번호 목록
Link : https://www.acmicpc.net/problem/5052
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    phone_number = list(input().strip() for _ in range(n))
    
    