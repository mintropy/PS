"""
Title : 독서실 거리두기
Link : https://www.acmicpc.net/problem/20665
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_best_seat(N: int, dokseosil_seat: list) -> int:
    left = 1
    best_seat = 0
    longest_dist = 0
    for i in range(2, N + 1):
        if dokseosil_seat[i]:
            # 1칸 차이라면 넘어가기
            if i - left == 1:
                left = i
            # 아니라면 가능한 자리인지 탐색
            else:
                total_dist = i - left - 1
                # 가장 멀리 앉을 수 있는 거리 탐색
                if total_dist % 2:
                    dist_between = total_dist // 2
                else:
                    dist_between = total_dist // 2 - 1
                # 지금 선택할 자리가 최선인지
                if dist_between > longest_dist:
                    longest_dist = dist_between
                    best_seat = left + dist_between + 1
    # 마지막 자리가 유망한지 확인
    if not dokseosil_seat[N] and N - left - 1 > longest_dist:
        best_seat = N
    return best_seat


N, T, P = MIIS()
# 들어오는 시간 같다면, 나가는 시간 순서대로 확인해야됨
dokseosil_in = []
# 나가는 시간 확인
dokseosil_out = []
for i in range(T):
    in_time, out_time = MIIS()
    in_time = 60 * (in_time // 100) + in_time % 100
    out_time = 60 * (out_time // 100) + out_time % 100
    dokseosil_in.append((in_time, out_time, i + 1))
    dokseosil_out.append((out_time, i + 1))
dokseosil_in.sort()
dokseosil_out.sort()
in_idx = out_idx = 0

dokseosil_seat = [0] * (N + 1)
dokseosil_seat_by_idx = {i: 0 for i in range(1, T + 1)}
mingyu_seat = True
now = 60 * 9
result = 0
while now < 60 * 21:
    # 먼저 퇴실하고 입실 처리
    # 들어올 사람 없으면 모든 사람 나가기
    if in_idx == T:
        while out_idx < T:
            next_time, idx = dokseosil_out[out_idx]
            # 다음 사람 갈때까지 민규 좋아하는 자리 확인
            if mingyu_seat:
                result += next_time - now
                now = next_time
            else:
                now = next_time
            # 나가기 처리
            seat = dokseosil_seat_by_idx[idx]
            if seat == P:
                mingyu_seat = True
            out_idx += 1
        # 마지막 시간 처리
        result += 60 * 21 - now
        break
    # 다음 독서실 예약 인원 들어올 때까지 독서실에서 사람들 나가기
    # 다음 입장 사람 시간 보다 가장 먼저 나갈 사람 시간이 느린경우
    while dokseosil_in[in_idx][0] >= dokseosil_out[out_idx][0]:
        next_time, idx = dokseosil_out[out_idx]
        # 다음 사람 갈때까지 민규 좋아하는 자리 확인
        if mingyu_seat:
            result += next_time - now
            now = next_time
        else:
            now = next_time
        # 나가기 처리
        seat = dokseosil_seat_by_idx[idx]
        dokseosil_seat[seat] = 0
        if P == seat:
            mingyu_seat = True
        out_idx += 1
    # 아니라면 다음 사람 입장하기
    next_time, _, idx = dokseosil_in[in_idx]
    in_idx += 1
    # 다음 사람 들어오기까지 민규가 좋아하는 자리 비어있다면
    if mingyu_seat:
        result += next_time - now
    # 1번 자리가 비어있으면 1번 자리로, 아니면 자리 탐색
    if not dokseosil_seat[1]:
        dokseosil_seat[1] = idx
        dokseosil_seat_by_idx[idx] = 1
    else:
        seat = find_best_seat(N, dokseosil_seat)
        dokseosil_seat[seat] = idx
        dokseosil_seat_by_idx[idx] = seat
    now = next_time
    # 민규가 좋아하는 자리 차있는지
    if dokseosil_seat[P]:
        mingyu_seat = False
    else:
        mingyu_seat = True

print(result)
