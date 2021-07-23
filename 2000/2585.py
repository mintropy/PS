'''
Title : 경비행기
Link : https://www.acmicpc.net/problem/2585
'''

import sys, math, collections

input = sys.stdin.readline

def cal_len(st: list, end: list) -> int:
    return math.sqrt((st[0] - end[0]) ** 2 + (st[1] - end[1]) ** 2)

def bfs(airport: list, k: int) -> int:
    # 순서대로 위치한 점의 좌표, 지나친 비행장 수, 비행 여정 중 최대 주유량
    queue = collections.deque([(0, 0, 0, 0)])
    min_oil = 20000
    while queue:
        x, y, c, o = queue.popleft()
        if c == k:
            # 이동 거리
            move = cal_len([x, y], [10000, 10000])
            # 주유량
            if move % 10 < 1e-10:
                oil = move // 10
            else:
                oil = int(move // 10 + 1)
            total_oil = max(oil, o)
            min_oil = min(total_oil, min_oil)
            continue
        for x2, y2 in airport:
            if x2 < x or y2 < y:
                continue
            # 이동 거리
            move = cal_len([x, y], [x2, y2])
            # 주유량
            if move % 10 < 1e-10:
                oil = move // 10
            else:
                oil = int(move // 10 + 1)
            queue.append((x2, y2, c + 1, max(o, oil)))
    return min_oil

n, k = map(int, input().split())
airport = [list(map(int, input().split())) for _ in range(n)]
print(bfs(airport, k))
