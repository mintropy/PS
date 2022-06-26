"""
Title : 칵테일
Link : https://www.acmicpc.net/problem/1033
"""

from collections import deque
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    amounts = [0] * N
    queue = deque([tuple(map(int, input().split())) for _ in range(N - 1)])
    a, b, p, q = queue.popleft()
    amounts[a] = p
    amounts[b] = q
    while queue:
        a, b, p, q = queue.popleft()
        if not amounts[a] and not amounts[b]:
            queue.append((a, b, p, q))
            continue
        if not amounts[a]:
            a, b = b, a
            p, q = q, b
        amounts = [x * p for x in amounts]
        


"""
august14 캌테일, 재료 N개
재료 쌍 N - 1개의 비율 ㅇㅋ >> 전체 재료 비율

a, b 둘다 아직 비율이 없으면 넘어가기
a, b 중에 b를 입력해야하는 값으로 변경
> a값과 기존값들에 모두 p배


4 0 1 1
4 1 3 1
4 2 5 1
4 3 7 1

0 0 0 0 0
> 1 0 0 0 1
> 3 1 0 0 3
> 15 5 1 0 15
> 105 35 7 1 105


2 3 6 8 > 2 3 3 4
0 1 9 3 > 0 1 3 1
3 0 7 5 > 0 3 5 7

0 0 0 0
> 0 0 3 4
> 20 0 21 28
> 60 20 63 84
"""
