"""
Title : 직사각형
Link : https://www.acmicpc.net/problem/2527
"""


def check_no_overlap(rectangle1: list, rectangle2: list) -> bool:
    # rectangle2가 더 위에
    if rectangle2[2][1] > rectangle1[0][1]:
        return True
    # rectangle2가 더 아래
    elif rectangle2[0][1] < rectangle1[2][1]:
        return True
    # rectangle2가 더 오른
    elif rectangle2[0][0] > rectangle1[1][0]:
        return True
    # rectangle2가 더 왼
    elif rectangle2[1][0] < rectangle1[0][0]:
        return True
    return False


def check_point(rectangle1: list, rectangle2: list) -> bool:
    # 모서리가 만나는 가능한 4가지 경우 확인
    # rectangle1 기준 위 왼쪽/오른쪽, 아래 왼쪽/오른쪽 확인
    if rectangle1[0] == rectangle2[3]:
        return True
    elif rectangle1[1] == rectangle2[2]:
        return True
    elif rectangle1[2] == rectangle2[1]:
        return True
    elif rectangle1[3] == rectangle2[0]:
        return True
    return False


def check_line(rectangle1: list, rectangle2: list) -> bool:
    # retangle1 기준 위/오/아/왼 쪽 선분과 만나는지 확인
    # 이때 x 또는 y 좌표만 확인해도 됨
    # 만나지 않는 경우, 점인경우에서 아닌 상황 제외됨
    # 직사각형 위 아래와 만날 수 있지만, 포함되면 직사각형이 되므로, 한쪽 방향씩만 확인하면 됨
    if rectangle1[0][1] == rectangle2[2][1]:
        return True
    elif rectangle1[1][0] == rectangle2[0][0]:
        return True
    elif rectangle1[2][1] == rectangle2[0][1]:
        return True
    elif rectangle1[0][0] == rectangle2[1][0]:
        return True
    return False


for _ in range(4):
    x1, y1, x2, y2, a1, b1, a2, b2 = map(int, input().split())
    # 두 직사각형 네 점 확인
    # 순서대로 위 왼쪽/오른쪽, 아래 왼쪽 / 오른쪽
    rectangle1 = [
        (min(x1, x2), max(y1, y2)), 
        (max(x1, x2), max(y1, y2)), 
        (min(x1, x2), min(y1, y2)), 
        (max(x1, x2), min(y1, y2)) 
    ]
    rectangle2 = [
        (min(a1, a2), max(b1, b2)), 
        (max(a1, a2), max(b1, b2)), 
        (min(a1, a2), min(b1, b2)), 
        (max(a1, a2), min(b1, b2)) 
    ]
    
    # 경우를 하나씩 구분
    # 겹치지 않는 경우 : x, y 좌표중 하나라도 더 크거나 작음
    # rectangle1 기준으로 rectangle2가 더 위/오/아/왼쪽에 있는지 확인
    if check_no_overlap(rectangle1, rectangle2):
        print('d')
    # 점으로 만나는 경우
    elif check_point(rectangle1, rectangle2):
        print('c')
    # 선분으로 만나는 경우
    elif check_line(rectangle1, rectangle2):
        print('b')
    # 그 외의 경우
    else:
        print('a')
