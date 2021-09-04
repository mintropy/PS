"""
Title : 팩토리얼 0의 개수
Link : https://www.acmicpc.net/problem/1676
"""

n = int(input())
count = n // 5 + n // 25 + n // 125
print(count)
