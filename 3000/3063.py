"""
Title : 게시판
Link : https://www.acmicpc.net/problem/3063
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    # 영화 동아리 포스터 크기
    sang = (x2 - x1) * (y2 - y1)
    
    # 영화 포스터가 완전히 덮힐 때
    if x1 >= x3 and y1 >= y3 and x2 <= x4 and y2 <= y4:
        print(0)
    # 하나도 겹치지 않는 경우
    elif x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:
        print(sang)
    # 일부만 덮는 경우, 덮히는 부분 계산
    # 일부만 덮힌다면, 곂치는 선분은 2개
    else:
        if x1 < x3 < x2:
            x_left = x3
        else:
            x_left = x1
        if x1 < x4 < x2:
            x_right = x4
        else:
            x_right = x2
        
        if y1 < y3 < y2:
            y_down = y3
        else:
            y_down = y1
        if y1 < y4 < y2:
            y_up = y4
        else:
            y_up = y2
        
        sang -= (x_right - x_left) * (y_up - y_down)
        print(sang)
