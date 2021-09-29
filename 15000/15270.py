"""
Title : 친구 팰린드롬
Link : https://www.acmicpc.net/problem/15270
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(friends_check: list, friends_pairs: int, friends_count: int) -> int:
    # 지금까지 확인한 친구 수 friends_count
    # 무대에 올라간 친구 쌍 friends_paris
    global n, m, friends
    # 모든 친구 무대 올림
    if friends_count == n:
        return 0
    max_pairs = 0
    pairs_check = False
    # 남은 친구 순회하며 올리기
    for i in range(1, n + 1):
        # 무대에 올라가지 않은 학생인 경우
        if not friends_check[i]:
            for j in friends[i]:
                # 친구가 무대에 올라가지 않은 경우
                if not friends_check[j]:
                    friends_check[i] = True
                    friends_check[j] = True
                    pairs = dfs(friends_check, friends_pairs + 1, friends_count + 2)
                    friends_check[i] = False
                    friends_check[j] = False
                    pairs_check = True
                    if pairs > max_pairs:
                        max_pairs = pairs
    # 모든 친구 확인, 남은 친구 쌍 없는 경우
    if not pairs_check:
        max_pairs = dfs(friends_check, friends_pairs, n)
    return friends_pairs + max_pairs


n, m = MIIS()
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = MIIS()
    friends[u].append(v)
    friends[v].append(u)

pairs = dfs([False] * (n + 1), 0, 0)

# 친구 쌍의 수 * 2 == 친수 수 >> 친구 수 출력
if pairs * 2 == n:
    print(n)
# 친구가 홀수 >> 어떻게 하든지 한 명 남음(로봇춤)
# 친구수 짝수 >> 한명이 남는 경우에만 여기로 내려옴
else:
    print(pairs * 2 + 1)
