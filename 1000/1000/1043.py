"""
Title : 거짓말
Link : https://www.acmicpc.net/problem/1043
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, m = MIIS()
wise_guy_count, *wise_guy = MIIS()

count_lie_story = 0

# 이야기 아는 사람은 0으로
parents = list(range(n + 1))
for p in wise_guy:
    parents[p] = 0

for _ in range(m):
    party_people_count, *party_people = MIIS()
    for p in party_people:
        pass

