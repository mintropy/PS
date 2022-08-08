"""
Title : 최종 순위
Link : https://www.acmicpc.net/problem/3665
"""

from collections import deque
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    for _ in range(II()):
        N = II()
        grades = list(MIIS())
        M = II()
        changed_grades = set(tuple(MIIS()) for _ in range(M))

        teams = [[] for _ in range(N + 1)]
        teams_before = [0] * (N + 1)
        for i in range(N):
            for j in range(i + 1, N):
                a, b = grades[i], grades[j]
                if (a, b) in changed_grades or (b, a) in changed_grades:
                    a, b = b, a
                teams[a].append(b)
                teams_before[b] += 1

        queue = deque([])
        for i in range(1, N + 1):
            if not teams_before[i]:
                queue.append((i))
        if not queue:
            print("IMPOSSIBLE")
            continue
        ans = []
        while queue and len(ans) < N:
            if len(queue) >= 2:
                break
            x = queue.popleft()
            ans.append(x)
            for y in teams[x]:
                teams_before[y] -= 1
                if not teams_before[y]:
                    queue.append(y)
                elif teams_before[y] < 0:
                    break
            else:
                continue
            break
        if len(ans) == N:
            print(*ans)
        else:
            print("IMPOSSIBLE")
