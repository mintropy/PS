"""
Title : 음하철도 구구팔
Link : https://www.acmicpc.net/problem/1393
"""

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

gcd_dx_dy = gcd(dx, dy)
dx //= gcd_dx_dy
dy //= gcd_dx_dy

dist = (xs - xe) ** 2 + (ys - ye) ** 2

k = 1
while True:
    dist1 = (xs - xe - k * dx ) ** 2 + (ys - ye - k * dy) ** 2
    if dist > dist1:
        dist = dist1
        k += 1
    else:
        print(xe + dx * (k - 1), ye + dy * (k - 1))
        break
