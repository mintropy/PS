"""
Title : 귀여운 라이언
Link : https://www.acmicpc.net/problem/15565
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

# 최솟값
min_sub_seq = int(1e6)

# 투 포인터
st, end = -1, -1
# st에서 end까지 라이언 인형 개수
lion_count = 0

while True:
    # 종료 조건
    if end == n - 1 and lion_count <= k - 1:
        break
    # 라이언 인형을 원하는 만큼 모았을 때
    if lion_count >= k:
        if end - st + 1 < min_sub_seq:
            min_sub_seq = end - st + 1
        if seq[st] == 1:
            lion_count -= 1
        st += 1
    elif lion_count < k:
        end += 1
        if seq[end] == 1:
            lion_count += 1

print(min_sub_seq)