"""
Title : 집배원 한상덕
Link : https://www.acmicpc.net/problem/2842
"""

from collections import deque
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    town = [input().strip() for _ in range(N)]
    heights_map = [list(map(int, input().split())) for _ in range(N)]
    heights = sorted(set(sum(heights_map, [])))
    if len(heights) == 1:
        print(0)
        exit()
    heights = [heights[0]] + heights + [heights[-1]]

    post = tuple()
    houses = 0
    house_min_heights, house_max_heights = 1_000_000, 0
    for i, line in enumerate(town):
        for j, x in enumerate(line):
            if x == "P":
                post = (i, j)
                h = heights_map[i][j]
                if house_min_heights > h:
                    house_min_heights = h
                if house_max_heights < h:
                    house_max_heights = h
            elif x == "K":
                houses += 1
                h = heights_map[i][j]
                if house_min_heights > h:
                    house_min_heights = h
                if house_max_heights < h:
                    house_max_heights = h
    left, right = 1, len(heights) - 2
    ans = heights[-1] - heights[0]
    delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    while left <= right:
        min_height, max_height = heights[left], heights[right]
        queue = deque([post])
        houses_check = 0
        visited = [[False] * N for _ in range(N)]
        while queue:
            x, y = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if town[x][y] == "K":
                houses_check += 1
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny]:
                        continue
                    if min_height <= heights_map[nx][ny] <= max_height:
                        queue.append((nx, ny))
            ans = heights[right] - heights[left]
            if min_height == house_min_heights and max_height == house_max_heights:
                break
            left_diff = heights[left + 1] - heights[left]
            right_diff = heights[right] - heights[right - 1]
            if left_diff > right_diff:
                if max_height == house_max_heights:
                    left += 1
                else:
                    right -= 1
            else:
                if min_height == house_min_heights:
                    right -= 1
                else:
                    left += 1
        else:
            break
    print(ans)
