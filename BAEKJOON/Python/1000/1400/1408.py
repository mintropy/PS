"""
Title : 24
Link : https://www.acmicpc.net/problem/1408
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    now = list(map(int, input().strip().split(":")))
    start = list(map(int, input().strip().split(":")))

    now_sec = now[0] * 60 * 60 + now[1] * 60 + now[2]
    start_sec = start[0] * 60 * 60 + start[1] * 60 + start[2]
    if now_sec < start_sec:
        ans_sec = start_sec - now_sec
    else:
        ans_sec = 24 * 60 * 60 - (now_sec - start_sec)

    ans = [0] * 3
    ans[0] = ans_sec // (60 * 60)
    ans_sec %= 60 * 60
    ans[1] = ans_sec // 60
    ans_sec %= 60
    ans[2] = ans_sec

    make_num = lambda x: str(x).zfill(2)
    result = ":".join(map(make_num, ans))
    print(result)

'''
13:52:30
14:00:00
ans : 00:07:30

14:00:00
13:52:30
ans : 23:52:30
'''
