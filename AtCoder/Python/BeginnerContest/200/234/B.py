import sys
input = sys.stdin.readline


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

max_length_sq = 0
for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if max_length_sq < dist:
            max_length_sq = dist

print(max_length_sq ** 0.5)
