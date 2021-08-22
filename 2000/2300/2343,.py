"""
Title : 기타 레슨
Link : https://www.acmicpc.net/problem/2343
"""

import sys
input = sys.stdin.readline


def bin_search(m, lessons):
    st, end = max(lessons), sum(lessons)
    ans = sum(lessons)
    while st <= end:
        mid = (st + end) // 2
        # mid길이로 m개 가능한지
        blue_ray_count = 0
        blue_ray_now = mid
        for l in lessons:
            if l > blue_ray_now:
                blue_ray_count += 1
                if blue_ray_count > m:
                    break
                blue_ray_now = mid - l
            else:
                blue_ray_now -= l
        else:
            blue_ray_count += 1
        # 확인
        if blue_ray_count <= m:
            if ans > mid:
                ans = mid
            end = mid - 1
        else:
            st = mid + 1
    print(ans)
    return


_, m = map(int, input().split())
lessons = list(map(int, input().split()))

bin_search(m, lessons)
