"""
Title : 인지융~
Link : https://www.acmicpc.net/problem/24727
"""

from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    C, E = map(int, input().split())
    
    my_map = [[0] * N for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    queue = deque([(0, 0)])
    while queue:
        if not C:
            break
        x, y = queue.popleft()
        if my_map[x][y]:
            continue
        my_map[x][y] = 1
        C -= 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                queue.append((nx, ny))
    queue = deque([(N - 1, N - 1)])
    while queue:
        if not E:
            break
        x, y = queue.popleft()
        if (
            my_map[x][y]
            or (x > 0 and my_map[x - 1][y] == 1)
            or (y > 0 and my_map[x][y - 1] == 1)
        ):
            continue
        my_map[x][y] = 2
        E -= 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                queue.append((nx, ny))
    
    if E:
        print(-1)
    else:
        print(1)
        for line in my_map:
            print(*line)

'''
https://prod.velog.io/@cldhfleks2/24727

5
17 4

5
18 4

2 
1 1

3
3 3

4
6 6

4
7 5
'''