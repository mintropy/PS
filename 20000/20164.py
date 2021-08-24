"""
Title : 홀수 홀릭 호석
Link : https://www.acmicpc.net/problem/20164
"""

import sys
input = sys.stdin.readline


def count_odd(num: list) -> int:
    count = 0
    for m in num:
        if m % 2:
            count += 1
    return count


def list_to_num(num: list) -> int:
    num.reverse()
    ans = 0
    while num:
        ans *= 10
        ans += num.pop()
    return ans


def search(num: list) -> tuple:
    # 최솟값, 최댓값 리턴
    # 길이가 1이면 리턴
    if len(num) == 1:
        return 0, 0
    # 두자리 수이면, 둘로 나누어 계산
    elif len(num) == 2:
        tmp = list(int(i) for i in str(sum(num)))
        cnt = count_odd(tmp)
        return cnt, cnt
    # 길이가 3이상이면 세 조각으로 구분, 재귀 실행
    else:
        min_count, max_count = 10 ** 3, 0
        # 구분할 구간
        for left in range(1, len(num) - 1):
            for right in range(left + 1, len(num)):
                # 세 구간으로 분할
                left_nums = num[:left]
                mid_nums = num[left:right]
                right_nums = num[right:]
                # 해당 구간을 숫자로 표현
                l = list_to_num(left_nums)
                m = list_to_num(mid_nums)
                r = list_to_num(right_nums)
                # 각 구분된 구간의 합으로 다음 과정 시행
                next_num = list(int(i) for i in str(sum((l, m, r))))
                next_cnt = count_odd(next_num)
                next_min, next_max = search(next_num)
                # 최대 최소 비교
                if next_cnt + next_min < min_count:
                    min_count = next_cnt + next_min
                if next_cnt + next_max > max_count:
                    max_count = next_cnt + next_max
        return min_count, max_count



num = list(int(i) for i in input().strip())
odd_count = count_odd(num)

min_count, max_count = search(num)
print(min_count + odd_count, max_count + odd_count)
