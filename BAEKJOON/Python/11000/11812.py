"""
Title : K진 트리
Link : https://www.acmicpc.net/problem/11812
"""

# TypeError
import sys, bisect
input = sys.stdin.readline


def find_parent(point, depth):
    if depth == 1:
        return 1
    for i in range(depth + 1):
        if left_most[depth] + (k ** (depth - 1)) * i <= point < left_most[depth] + (k ** (depth - 1)) * (i + 1):
            j = (k ** (depth - 2) * i) + (point - (left_most[depth] + (k ** (depth - 1)) * i)) // 3
            return left_most[depth - 1] + j


n, k, q = map(int, input().split())
if k == 1:
    for _ in range(q):
        a, b = map(int, input().split())
        print(abs(a - b))
    exit()

# 각 트리의 i높이에서 가장 왼쪽 노드
left_most = [1, 2]
d = 1
while True:
    now =left_most[-1] + k ** d
    d += 1
    left_most.append(now)
    if now > n:
        break


for _ in range(q):
    x, y = map(int, input().split())
    # 두 점의 깊이
    depth_x = bisect.bisect_left(left_most, x)
    depth_y = bisect.bisect_left(left_most, y)
    if x != left_most[depth_x]:
        depth_x -= 1
    if y != left_most[depth_y]:
        depth_y -= 1
    # 두 점의 거리
    dist = 0
    # 깊이 맞춰주기
    while depth_x != depth_y:
        if depth_x < depth_y:
            y = find_parent(y, depth_y)
            depth_y -= 1
        else:
            x = find_parent(x, depth_x)
            depth_x -=1
        dist += 1
    # 점이 같아질때까지 탐색
    while x != y:
        x = find_parent(x, depth_x)
        y = find_parent(y, depth_y)
        depth_x -= 1
        depth_y -= 1
        dist += 2
    print(dist)


'''
9876543210 3 10
5 40

'''