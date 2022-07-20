"""
Title : 놀이공원
Link : https://www.acmicpc.net/problem/2594
"""

from sys import stdin

input = stdin.readline


def get_time_diff(left: int, right: int) -> int:
    if left // 100 == right // 100:
        return right - left
    if left % 100:
        diff = (60 - (left % 100)) + (right % 100)
        left, right = (left // 100) * 100 + 100, (right // 100) * 100
    else:
        diff = right % 100
        right = (right // 100) * 100
    diff += ((right - left) // 100) * 60
    return diff


if __name__ == "__main__":
    N = int(input())
    schedules = []
    for _ in range(N):
        st, end = map(int, input().split())
        if st % 100 < 10:
            st = st - 100 + 50
        else:
            st -= 10
        if end % 100 >= 50:
            end = end + 100 - 50
        else:
            end += 10
        schedules.append((st, end))
    schedules.sort()
    ans = 0
    time = 1000
    for st, end in schedules:
        if time < st:
            ans = max(ans, get_time_diff(time, st))
        if time < end:
            time = end
    else:
        if time < 2200:
            ans = max(ans, get_time_diff(time, 2200))
    print(ans)
