"""
Title : 열혈강호
Link : https://www.acmicpc.net/problem/11375
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bipartite_matching(l):
    global left, right, visited
    visited[l] = True
    for r in left[l]:
        if not right[r]:
            right[r] = l
            return True
    for r in left[l]:
        if not visited[right[r]] and bipartite_matching(right[r]):
            right[r] = l
            return True
    return False


if __name__ == "__main__":
    N, M = MIIS()
    left = [[]]
    for _ in range(N):
        _, *works = MIIS()
        left.append(tuple(works))
    right = [0] * (M + 1)
    ans = 0
    for l in range(1, N + 1):
        visited = [False] * (N + 1)
        if bipartite_matching(l):
            ans += 1
            if ans == M:
                break
    print(ans)


# python TLE, pypy AC
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(person):
    global people, works, visited
    if visited[person]:
        return False
    visited[person] = True
    for work in people[person]:
        if not works[work] or dfs(works[work]):
            works[work] = person
            return True
    return False


if __name__ == "__main__":
    N, M = MIIS()
    people = [[]]
    for _ in range(N):
        _, *works = MIIS()
        people.append(tuple(works))
    works = [0] * (M + 1)
    for person in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(person)
    print(M + 1 - works.count(0))
