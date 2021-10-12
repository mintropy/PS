"""
Title : 마법사 상어와 블리자드
Link : https://www.acmicpc.net/problem/21611
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def square_to_linear(n: int, magical_map: int) -> list:
    # 기본 지도를 선형으로 저장
    magical_linear_map = [0] * (n ** 2)
    # 탐색 방향, 길이
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    search = [i // 2 for i in range(2, n * 2 + 1)]
    search[-1] -= 1
    # 선형 지도에 넣을 위치
    idx = 1
    # 정 사각형 지도에서 지금 위치, 방향
    d = 0
    x = y = n // 2
    for s in search:
        # s칸만큼 앞으로 진행
        for _ in range(s):
            # 한 칸 앞으로
            x, y = x + dx[d], y + dy[d]
            # 해당 칸의 숫자 저장
            magical_linear_map[idx] = magical_map[x][y]
            idx += 1
        # 방향 회전
        d = (d + 1) % 4
    return magical_linear_map


def freeze_balls(magical_linear_map: list, d: int, s: int, linear_idx: list):
    # 마법을 사용해서 구슬 파괴
    for i in range(s):
        magical_linear_map[linear_idx[d][i]] = 0


def ball_front_explode(n: int, magical_linear_map: list):
    while True:
        # 지금 탐색하는 비어있는 자리 left, 앞으로 당겨야 하는 구슬 자리 right
        left, right = 1, 1
        # 폭발이 있었는지
        is_explode = False
        # 지금 확인 하는 숫자, 연속 개수
        ball_num_now = 0
        ball_continuous = 0
        while left < n ** 2 and right < n ** 2:
            
            pass
        
        if not is_explode:
            return


n, m = MIIS()
magical_map = [list(MIIS()) for _ in range(n)]

# 지도를 선형으로 바꾸어 탐색
magical_linear_map = square_to_linear(n, magical_map)
# 각 방향이 주어졌을 때 확인해야하는 인덱스
linear_idx = [[], [7, 22], [3, 14], [1, 10], [5, 18]]
# 인덱스 추가적 생성
for _ in range(7, n + 1, 2):
    for i in range(1, 4 + 1):
        l1, l2 = linear_idx[i][-1], linear_idx[i][-2]
        linear_idx[i].append(l1 + (l1 - l2 + 8))

score = 0
# 블리자드 실행
for _ in range(m):
    d, s = map(int, input().split())
    # d방향 s칸에 구슬 파괴
    freeze_balls(magical_linear_map, d, s, linear_idx)
    # 구슬 앞으로 & 폭발
    
    # 구슬 변화
    

print(score)
