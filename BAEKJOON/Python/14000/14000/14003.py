"""
Title : 가장 긴 증가하는 부분 수열 5
Link : https://www.acmicpc.net/problem/14003
"""

import sys
input = sys.stdin.readline

"""
counter example
10
3 1 4 2 7 5 8 6 10 1
output : 3 2 5 6 10
"""


def bin_search(i: int, s: int):
    global n, lower_bound, lower_bound_idx
    # 가장 큰 수이면 마지막에 추가
    if s > lower_bound[-1]:
        lower_bound.append(s)
        lower_bound_idx[i] = len(lower_bound)
    elif s == lower_bound[-1]:
        lower_bound_idx[i] = len(lower_bound)
    else:
        left = 0
        want = right = len(lower_bound) - 1
        while left <= right:
            mid = (left + right) // 2
            if lower_bound[mid] >= s:
                if want > mid:
                    want = mid
                right = mid - 1
            elif lower_bound[mid] < s < lower_bound[mid + 1]:
                want = mid + 1
                break
            else:
                left = mid + 1
        lower_bound[want] = s
        lower_bound_idx[i] = want + 1


n = int(input())
seq = list(map(int, input().split()))

# lower_bound를 탐색, 저장하는 리스트
lower_bound = [seq[0]]
# lower_bound에 나타나는 인덱스를 저장하는 리스트
lower_bound_idx = [1] * n

# 수열을 2번째부터 탐색 시작
for i in range(1, n):
    # if len(lower_bound) == 1:
    #     s = seq[i]
    #     if s > lower_bound[0]:
    #         lower_bound.append(s)
    #         lower_bound_idx[i] = 2
    #     else:
    #         lower_bound[0] = s
    # else:
    bin_search(i, seq[i])

min_sub_seq = []
idx = len(lower_bound)

for i in range(n - 1, -1, -1):
    if idx == 0:
        break
    if lower_bound_idx[i] == idx:
        min_sub_seq.append(seq[i])
        idx -= 1

print(len(min_sub_seq))
min_sub_seq.reverse()
print(*min_sub_seq)