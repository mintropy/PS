"""
Title : 게리맨더링
Link : https://www.acmicpc.net/problem/17471
"""

from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def make_section(N: int, comb: tuple) -> list:
    section = [1] * (N + 1)
    section[0] = 3
    for x in comb:
        section[x] = 2
    return section


def search(
    N: int, sections: list[list[int]], populations: list[int], section: list[int]
) -> tuple[int]:
    pop_a = pop_b = 0
    visited = [False] * (N + 1)
    visited[0] = True
    queue = deque([section.index(1), section.index(2)])
    while queue:
        x = queue.popleft()
        if visited[x]:
            continue
        visited[x] = True
        s = section[x]
        if s == 1:
            pop_a += populations[x]
        elif s == 2:
            pop_b += populations[x]
        for y in sections[x]:
            if section[y] != s:
                continue
            if not visited[y]:
                queue.append(y)
    if all(visited):
        return pop_a, pop_b
    else:
        return 0, 0


def get_diff(x: int, y: int) -> int:
    return abs(x - y)


if __name__ == "__main__":
    N = int(input())
    populations = [0] + list(MIIS())
    sections = [[]]
    for i in range(N):
        _, *section = MIIS()
        sections.append(list(section))
    ans = 1000
    for i in range(1, N):
        for comb in combinations(range(1, N + 1), i):
            section = make_section(N, comb)
            x, y = search(N, sections, populations, section)
            if not x and not y:
                continue
            tmp = get_diff(x, y)
            if ans > tmp:
                ans = tmp
    print(ans if ans != 1000 else -1)
