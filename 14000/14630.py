"""
Title : 변신로봇
Link : https://www.acmicpc.net/problem/14630
"""

import sys
input = sys.stdin.readline


def count_cost(before, after):
    result = 0
    for i in range(len(before)):
        result += (int(before[i]) - int(after[i])) ** 2
    return result



n = int(input())
status = [tuple(input().strip().split()) for _ in range(n)]

st, end = map(int, input().split())
st -= 1
end -= 1


min_cost = 10 ** 8

# i번째 변신상태를 j번째 하는 최소 비용
cost_by_change = [[min_cost] * n for _ in range(n)]

# i번째로 해당 변신상태로 변할 때
for i in range(n - 1):
    # j번 형태로 변하는 비용
    for j in range(n):
