"""
Title : 순열의 순서
Link : https://www.acmicpc.net/problem/1722
"""

import sys
input = sys.stdin.readline


N = int(input())
factorial = [1, 1]
for i in range(2, N + 1):
    factorial.append(i * factorial[-1])
cmd, *query = map(int, input().split())

if cmd == 1:
    query = query[0]
    num_check = [False] * (N + 1)
    perm = []
    while query:
        if query == factorial[-1]:
            for i in range(N, 0, -1):
                if not num_check[i]:
                    num_check[i] = True
                    perm.append(i)
            break
        else:
            factorial.pop()
        # 가장 큰 팩토리얼보다 큰 만큼 횟수 탐색
        count = query // factorial[-1]
        if not query % factorial[-1]:
            count -= 1
        for i in range(1, N + 1):
            if not num_check[i]:
                if count == 0:
                    perm.append(i)
                    num_check[i] = True
                    break
                else:
                    count -= 1
        query %= factorial[-1]
    # 남은 숫자 추가
    for i in range(N, 0, -1):
        if not num_check[i]:
            perm.append(i)
    print(*perm)
else:
    factorial.pop()
    count = 0
    query.reverse()
    num_check = [False] * (N + 1)
    while query:
        for i in range(1, N + 1):
            if i == query[-1]:
                num_check[i] = True
                factorial.pop()
                query.pop()
                break
            elif not num_check[i]:
                count += factorial[-1]
    print(count + 1)
