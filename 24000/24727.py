"""
Title : 인지융~
Link : 
"""

import sys
input = sys.stdin.readline


def count_walls(x):
    count = 2
    now = 1
    while True:
        if x <= now:
            return count
        now += count
        count += 1


if __name__ == "__main__":
    N = int(input())
    C, E = map(int, input().split())
    
    total = C + E
    min_count = min(C, E)
    walls = count_walls(min_count)
    if total + walls > N * N:
        print(-1)
    else:
        my_map = [[0] * N for _ in range(N)]
        for i in range(N):
            if not C:
                break
            for j in range(i + 1):
                if not C:
                    break
                my_map[i - j][j] = 1
                C -= 1
        for i in range(1, N):
            if not C:
                break
            for j in range(N - i - 1):
                if not C:
                    break
                my_map[N - 1 - j][j + 1] = 1
                C -= 1
        for i in range(N):
            if not E:
                break
            for j in range(i + 1):
                if not E:
                    break
                my_map[N - 1 - i + j][N - 1 - j] = 2
                E -= 1
        for i in range(1, N):
            if not E:
                break
            for j in range(N - i - 1):
                if not E:
                    break
                my_map[j][N - 2 - j]
                E -= 1
        for line in my_map:
            print(*line)
