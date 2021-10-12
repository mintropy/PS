"""
Title : 마법사 상어와 블리자드
Link : https://www.acmicpc.net/problem/21611
"""

import collections
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


def freeze_balls(magical_linear_map: list, d: int, s: int, linear_idx: list) -> list:
    # 마법을 사용해서 구슬 파괴
    for i in range(s):
        magical_linear_map[linear_idx[d][i]] = 0
    return magical_linear_map


def ball_front_explode(n: int, magical_linear_map: list) -> int:
    # 구슬이 폭발할때마다 점수를 저장해서 리턴
    score = 0
    while True:
        # 폭발이 있었는지
        is_explode = False
        # 채우기 시작하면 되는 시작 구간
        idx = 1
        # 지금 확인 하는 숫자, 연속 개수
        ball_num_now = 0
        ball_continuous = 0
        for i in range(1, n ** 2):
            # 빈공간이면 추가하고 넘어가기
            if magical_linear_map[i] == 0:
                continue
            # 새로운 공이 시작되거나, 기존과 같은 공일때
            elif ball_continuous == 0 or ball_num_now == magical_linear_map[i]:
                ball_num_now = magical_linear_map[i]
                ball_continuous += 1
            # 아니라면 폭발 or 채우기
            else:
                if ball_continuous >= 4:
                    score += ball_num_now * ball_continuous
                    is_explode = True
                else:
                    for _ in range(ball_continuous):
                        magical_linear_map[idx] = ball_num_now
                        idx += 1
                # 지금 위치에서 다시 공 개수 세는 카운트하기
                # 빈 공간일 때
                if magical_linear_map[i] == 0:
                    ball_continuous = 0
                # 아닐 때
                else:
                    ball_num_now = magical_linear_map[i]
                    ball_continuous = 1
        # 마지막 부분 입력 or 폭발
        if ball_continuous >= 4:
            score += ball_num_now * ball_continuous
            is_explode = True
        else:
            for _ in range(ball_continuous):
                magical_linear_map[idx] = ball_num_now
                idx += 1
        # 변화가 없을 때
        if not is_explode:
            return score, magical_linear_map
        # 남은 뒷공간 0으로
        magical_linear_map = magical_linear_map[:idx] + [0] * (n ** 2 - idx)


def new_balls(n: int, magical_linear_map: list) -> list:
    new_magical_linear_map = [0] * (n ** 2)
    # 새로 변하는 구슬 입력위치 인덱스
    idx_input = 1
    ball_num_now = 0
    ball_continuous = 0
    for i in range(1, n ** 2):
        # 더이상 변환하여 입력할 수 없을 때
        if magical_linear_map[i] == 0:
            break
        if idx_input == n ** 2:
            break
        # 같은 공이 연속될 때
        if ball_num_now == magical_linear_map[i]:
            ball_continuous += 1
        else:
            if ball_num_now != 0:
                # 이전 공에 대한 정보 처리
                new_magical_linear_map[idx_input] = ball_continuous
                new_magical_linear_map[idx_input + 1] = ball_num_now
                idx_input += 2
            # 새로운 공 정보 입력
            ball_num_now = magical_linear_map[i]
            ball_continuous = 1
    return new_magical_linear_map


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

totla_score = 0
# 블리자드 실행
for _ in range(m):
    d, s = map(int, input().split())
    # d방향 s칸에 구슬 파괴
    magical_linear_map = freeze_balls(magical_linear_map, d, s, linear_idx)
    # 구슬 앞으로 & 폭발
    score, magical_linear_map = ball_front_explode(n, magical_linear_map)
    totla_score += score
    # 구슬 변화
    magical_linear_map = new_balls(n, magical_linear_map)

print(totla_score)
