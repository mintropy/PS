"""
Title : 사전
Link : https://www.acmicpc.net/problem/1256
"""

import sys, math
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 전체 사전의 문자 개수
word_count = 0

# 전체 가능한 경우의 수
possibility = math.comb(m + n, n)

if possibility < k:
    print(-1)
else:
    result = ''
    # 한 문자씩 추가하며 계산
    # a가 이어 붙어질 때 원하는 순번에 도달하지 못하면 z 추가
    # 아니라면 a 추가
    for i in range(n + m):
        # 해당 경우의 수가 만족했을 때
        if word_count == k:
            result += 'a' * n + 'z' * m
            break
        # 또 다른 종료조건
        if n == 0 or m == 0:
            result += 'a' * n + 'z' * m
            break
        # 만족하지 않으면 계산
        # a가 이어 붙어질 때 경우의 수
        count_a = math.comb(n + m - 1, n - 1)
        if word_count + count_a < k:
            result += 'z'
            m -= 1
            word_count += count_a
        else:
            result += 'a'
            n -= 1
    
    print(result)