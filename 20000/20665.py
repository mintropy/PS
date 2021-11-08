"""
Title : 독서실 거리두기
Link : https://www.acmicpc.net/problem/20665
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_best_seat(N: int, dokseosil_seat: list) -> int:
    # 이전 채워져있는 왼쪽 자리
    left = 1
    best_seat = 0
    longest_dist = 0
    for i in range(2, N + 1):
        if not dokseosil_seat[i]:
            # 1칸 차이라면 넘어가기
            # 아니라면 가능한 자리인지 탐색
            if i > left + 1:
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
            # 이전 왼쪽 채워진 차리 설정
            left = i
    # 마지막 자리가 유망한지 확인
    # 마지막 자리가 비워져있고, 이전 거리보다 더 멀리 선택할 수 있을 때
    if dokseosil_seat[N] and N - left - 1 > longest_dist:
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
# 독서실 들어가는 시간 순서대로, 같다면 나가는 시간이 빠른 사람이 앞으로
# stack 구조로 뒤에서부터 빼면서 계산
dokseosil_in.sort(reverse=True)
dokseosil_out.sort(reverse=True)

# 지금 독서실 좌석 상태
dokseosil_seat = [False] + [True] * (N)
# i번 인덱스의 예약한 사람의 자리
dokseosil_seat_by_idx = {i: 0 for i in range(1, T + 1)}

now = 60 * 9
end_time = 60 * 21
result = 0

while now < end_time:
    # 더이상 들어올 사람이 없다면
    if not dokseosil_in:
        # 모든 사람 나가기
        while dokseosil_out:
            # 지금 민규가 좋아하는 자리 비어있는지
            if dokseosil_seat[P]:
                result += dokseosil_out[-1][0] - now
            # 다음 시간 확인 & 나가기 처리
            time, idx = dokseosil_out.pop()
            seat = dokseosil_seat_by_idx[idx]
            dokseosil_seat[seat] = True
            now = time
        # 남은 시간 더하기
        result += end_time - now
        break
    
    # 들어올 사람보다 먼저 or 같은 시간에 나가는 사람이 있다면
    while dokseosil_in[-1][0] >= dokseosil_out[-1][0]:
        # 지금 민규가 좋아하는 자리 비어있는지
        if dokseosil_seat[P]:
            result += dokseosil_out[-1][0] - now
        # 다음 시간 확인 & 나가기 처리
        time, idx = dokseosil_out.pop()
        seat = dokseosil_seat_by_idx[idx]
        dokseosil_seat[seat] = True
        now = time
    
    # 다음 한 사람 들어오기
    # 지금 시간부터 다음 사람 입장 시간까지 민규 자리 확인
    if dokseosil_seat[P]:
        result += dokseosil_in[-1][0] - now
    time, _, idx = dokseosil_in.pop()
    # 다음 사람 앉을 자리 확인
    # 1번 자리가 비어있음녀 1번 자리, 아니면 탐색
    if dokseosil_seat[1]:
        seat = 1
    else:
        seat = find_best_seat(N, dokseosil_seat)
    dokseosil_seat[seat] = False
    dokseosil_seat_by_idx[idx] = seat
    # 시간 변경
    now = time

print(result)


'''
# WA
def find_best_seat(N: int, dokseosil_seat: list) -> int:
    # 이전 채워져있는 왼쪽 자리
    left = 1
    best_seat = 0
    longest_dist = 0
    for i in range(2, N + 1):
        if dokseosil_seat[i]:
            # 1칸 차이라면 넘어가기
            # 아니라면 가능한 자리인지 탐색
            if i > left + 1:
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
            # 이전 왼쪽 채워진 차리 설정
            left = i
    # 마지막 자리가 유망한지 확인
    # 마지막 자리가 비워져있고, 이전 거리보다 더 멀리 선택할 수 있을 때
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
# 독서실 들어가는 시간 순서대로, 같다면 나가는 시간이 빠른 사람이 앞으로
dokseosil_in.sort()
dokseosil_out.sort()
in_idx = out_idx = 0

# 지금 독서실 좌석 상태
dokseosil_seat = [0] * (N + 1)
# i번 인덱스의 예약한 사람의 자리
dokseosil_seat_by_idx = {i: 0 for i in range(1, T + 1)}
mingyu_seat = True
now = 60 * 9
end_time = 60 * 21
result = 0
while now < end_time:
    # 먼저 퇴실하고 입실 처리
    # 들어올 사람 없으면 모든 사람 나가기
    if in_idx == T:
        while out_idx < T:
            next_time, idx = dokseosil_out[out_idx]
            # 다음 사람 갈때까지 민규 좋아하는 자리 확인
            if mingyu_seat:
                result += next_time - now
            now = next_time
            # 나가기 처리
            seat = dokseosil_seat_by_idx[idx]
            if seat == P:
                mingyu_seat = True
            out_idx += 1
        # 마지막 시간 처리
        result += end_time - now
        break
    # 다음 독서실 예약 인원 들어올 때까지 독서실에서 사람들 나가기
    # 다음 입장 사람 시간 보다 가장 먼저 나갈 사람 시간이 느린경우
    while dokseosil_in[in_idx][0] >= dokseosil_out[out_idx][0]:
        next_time, idx = dokseosil_out[out_idx]
        # 다음 사람 갈때까지 민규 좋아하는 자리 확인 & 시간 변경
        if mingyu_seat:
            result += next_time - now
        now = next_time
        # 나가기 처리
        seat = dokseosil_seat_by_idx[idx]
        dokseosil_seat[seat] = 0
        # 이전 사람 나간 자리가 민규가 좋아하는 자리였다면
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
'''
