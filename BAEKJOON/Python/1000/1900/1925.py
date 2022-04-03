"""
Title : 삼각형
Link : https://www.acmicpc.net/problem/1925
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

l1 = (x1- x2) ** 2 + (y1 - y2) ** 2
l2 = (x2- x3) ** 2 + (y2 - y3) ** 2
l3 = (x3- x1) ** 2 + (y3 - y1) ** 2
l1, l2, l3 = sorted([l1, l2, l3])

# 세 점이 일직선상에 있으면 삼각형 아님
if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
    print('X')
# 정삼각형
elif l1 == l2 and l2 == l3:
    print('JungTriangle')
# 두 변의 길이가 같을 때
elif l1 == l2 or l2 == l3 or l3 == l1:
    if l3 == l1 + l2:
        print('Jikkak2Triangle')
    elif l3 < l1 + l2:
        print('Yeahkak2Triangle')
    else:
        print('Dunkak2Triangle')
# 세 변의 길이가 다를 때
else:
    if l3 == l1 + l2:
        print('JikkakTriangle')
    elif l3 < l1 + l2:
        print('YeahkakTriangle')
    else:
        print('DunkakTriangle')
