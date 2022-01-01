"""
Title : 성싶당 밀키트
Link : https://www.acmicpc.net/problem/24041
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, G, K = MIIS()
important_ingredients = []
not_important_ingredients = []
for _ in range(N):
    ingredient = tuple(MIIS())
    if ingredient[2] == 0:
        important_ingredients.append(ingredient)
    else:
        not_important_ingredients.append(ingredient)




