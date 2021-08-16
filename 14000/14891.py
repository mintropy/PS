"""
Title : 톱니바퀴
Link : https://www.acmicpc.net/problem/14891
"""

import collections

gear1 = collections.deque(list(input().strip()))
gear2 = collections.deque(list(input().strip()))
gear3 = collections.deque(list(input().strip()))
gear4 = collections.deque(list(input().strip()))
gears = [[], gear1, gear2, gear3, gear4]

k = int(input())

gear_check = [
    [],
    [[], [2, 3, 4]],
    [[1], [3, 4]],
    [[2, 1], [4]],
    [[3, 2, 1], []]
]

for _ in range(k):
    gear, d = map(int, input().split())
    g_left, g_right = gears[gear][6], gears[gear][2]
    gears[gear].rotate(d)
    # 왼쪽 확인
    d_l = -d
    for i in gear_check[gear][0]:
        g_left1, g_right1 = gears[i][6], gears[i][2]    
        if g_left != g_right1:
            gears[i].rotate(d_l)
            d_l *= -1
            g_left = g_left1
        # 회전하기 전 이어진 두 칸이 같은 극일때
        else:
            break
    # 오른쪽 확인
    d_r = -d
    for i in gear_check[gear][1]:
        g_left2, g_right2 = gears[i][6], gears[i][2]    
        if g_right != g_left2:
            gears[i].rotate(d_r)
            d_r *= -1
            g_right = g_right2
        # 회전하기 전 이어진 두 칸이 같은 극일때
        else:
            break

ans = 0
for i in range(1, 5):
    ans += int(gears[i][0]) * 2 ** (i - 1)

print(ans)
