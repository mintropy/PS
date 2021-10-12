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


def ball_front_explode(n: int, magical_linear_map: list) -> int:
    # 구슬이 폭발할때마다 점수를 저장해서 리턴
    score = 0
    while True:
        # 지금 탐색하는 비어있는 자리 left, 앞으로 당겨야 하는 구슬 자리 right
        left = right = 1
        # 폭발이 있었는지
        is_explode = False
        # 지금 확인 하는 숫자, 연속 개수
        ball_num_now = 0
        ball_continuous = 0
        while left < n ** 2 and right < n ** 2:
            # left를 빈자리가 있을 때 까지 옮기기
            if magical_linear_map[left] != 0:
                left += 1
                if right <= left:
                    right = left + 1
            # right가 다른 구슬을 발견할때까지 옮기기
            elif magical_linear_map[right] == 0:
                right += 1
            else:
                # 새로 발견하는 구슬쌍인지, 아니면 기존 구슬 쌍인지
                if ball_continuous == 0:
                    ball_num_now = magical_linear_map[right]
                    ball_continuous = 1
                else:
                    # 기존 구슬이 연속되고 있었으면 앞의 연속되 구슬 확인
                    # 같은 종류 구슬이면 연속 + 1
                    # 다른 종류 구슬이면, 앞의 구슬이 폭발하는지 확인
                    if ball_num_now == magical_linear_map[right]:
                        ball_continuous += 1
                    else:
                        # 구슬 폭발
                        if ball_continuous >= 4:
                            score += ball_num_now * ball_continuous
                            is_explode = True
                        else:
                            for _ in range(ball_continuous):
                                magical_linear_map[left] = ball_num_now
                                left += 1
                        ball_continuous = 0
                # 오른쪽 자리 비워주고 이동
                magical_linear_map[right] = 0
                right += 1
        if not is_explode:
            return score


def new_balls(n: int, magical_linear_map: list) -> list:
    new_magical_linear_map = [0] * (n ** 2)
    # 새로 변하는 구슬 입력하는 인덱스, 구슬을 세는 인덱스
    idx_input = idx_read = 1
    while idx_input < n ** 2 and idx_read < n ** 2:
        # idx_read를 모두 움직여서 같은 구슬 쌍을 모두 탐색
        # 지금 확인 하는 숫자, 연속 개수
        ball_num_now = magical_linear_map[idx_read]
        ball_continuous = 1
        idx_read += 1
        while idx_read < n ** 2:
            if ball_num_now == magical_linear_map[idx_read]:
                ball_continuous += 1
                idx_read += 1
            else:
                break
        # 새로운 구슬로 입력
        new_magical_linear_map[idx_input] = ball_continuous
        new_magical_linear_map[idx_input + 1] = ball_num_now
        idx_input += 2
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

score = 0
# 블리자드 실행
for _ in range(m):
    d, s = map(int, input().split())
    # d방향 s칸에 구슬 파괴
    freeze_balls(magical_linear_map, d, s, linear_idx)
    # 구슬 앞으로 & 폭발
    score += ball_front_explode(n, magical_linear_map)
    # 구슬 변화
    magical_linear_map = new_balls(n, magical_linear_map)

print(score)
