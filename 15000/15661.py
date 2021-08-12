"""
Title : 링크와 스타트
Link : https://www.acmicpc.net/problem/15661
"""

import sys, itertools
input = sys.stdin.readline

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

team = [0] * (1<<n)

# 한 팀의 멤버 수
for member_count in range(2, n + 1):
    for comb in list(itertools.combinations(range(0, n), member_count)):
        # 해당 조합의 팀 점수
        team_mate_score = 0
        for i in range(member_count - 1):
            for j in range(i + 1, member_count):
                x, y = comb[i], comb[j]
                team_mate_score += (ability[x][y] + ability[y][x])
        team_num = 0
        for i in comb:
            team_num += 1 << i
        team[team_num] = team_mate_score

min_ability_diff = 10 ** 8
for t in range(1<<n):
    ability_diff = abs(team[t] - team[((1<<n) - 1) & ~t])
    if ability_diff < min_ability_diff:
        min_ability_diff = ability_diff

print(min_ability_diff)