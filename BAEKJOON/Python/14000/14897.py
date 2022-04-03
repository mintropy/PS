'''
Title : 톱니바퀴
Link : https://www.acmicpc.net/problem/14891
'''

import sys

input = sys.stdin.readline

def rotate_one(g: str, r: int) -> str:
    if r == -1:
        a, b = g[0], g[1:]
        return b + a
    elif r == 1:
        a, b = g[:-1], g[-1]
        return b + a

def rotate(gear: list, cmd: list):
    # 회전하는 톱니 번호, 방향
    n, r = cmd
    gear[n - 1] = rotate_one(gear[n - 1], r)
    # 왼쪽 확인
    pos = n
    r2 = r
    while True:
        pos -= 1
        if pos < 1:
            break
        if gear[pos + 1][6] == gear[pos][2]:


    # 오른쪽 확인


def score(gear: list) -> int:
    result = 0
    for i in range(4):
        if gear[i][0] == '1':
            result += 2 ** i
    return result

gear = [str(input()) for _ in range(4)]
k = int(input())
cmd = [list(map(int, input().split())) for _ in range(k)]

 