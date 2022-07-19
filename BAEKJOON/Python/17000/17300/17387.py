"""
Title : 선분 교차 2
Link : https://www.acmicpc.net/problem/17387
"""


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


# 첫 직선 기준 가능한지 확인
d1 = (y1 - y2) * (x3 - x1) + (x2 - x1) * (y3 - y1)
d2 = (y1 - y2) * (x4 - x1) + (x2 - x1) * (y4 - y1)

# 두번째 직선 기준 가능한지 확인
d3 = (y4 - y3) * (x1 - x3) + (x3 - x4) * (y1 - y3)
d4 = (y4 - y3) * (x2 - x3) + (x3 - x4) * (y2 - y3)

# 기울기
# 첫번째 직선의 기울기


# 겹칠 수 없을 때
if (min(x3, x4) > max(x1, x2)) or (max(x3, x4) < min(x1, x2))\
    or (min(y3, y4) > max(y1, y2)) or (max(y3, y4) < min(y1, y2)):
    print(0)
# 같은 점이 있는 경우
elif (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3)\
    or (x1 == x4 and y1 == y4) or (x2 == x4 and y2 == y4):
    print(1)
# 한 선분위에 있는 경우
elif (x1 < x3 < x2 and y1 < y3 < y2)\
    and ((y3 - y1) * (x2 - x3) == (y2 - y3) * (x3 - x1)):
    print(1)
elif (x1 < x4 < x2 and y1 < y4 < y2)\
    and ((y4 - y1) * (x2 - x4) == (y2 - y4) * (x4 - x1)):
    print(1)
elif (x3 < x1 < x4 and y3 < y1 < y4)\
    and ((y1 - y3) * (x4 - x1) == (y4 - y1) * (x1 - x3)):
    print(1)
elif (x3 < x2 < x4 and y3 < y2 < y4)\
    and ((y2 - y3) * (x4 - x2) == (y4 - y2) * (x2 - x3)):
    print(1)
# 두 값이 모두 양수 / 음수인 경우 불가능
elif (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0):
    print(0)
elif (d3 < 0 and d4 < 0) or (d3 > 0 and d4 > 0):
    print(0)
else:
    print(1)
