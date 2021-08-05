"""
Title : 차집합
Link : https://www.acmicpc.net/problem/1822
"""

a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

set_a -= set_b
list_a = sorted(set_a)
print(len(list_a))
print(*list_a)