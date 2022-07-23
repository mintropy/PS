import sys

input = sys.stdin.readline

l, r = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

count = 0
x, y = l, l
while True:
    if y == r:
        x += 1
        y = x
    else:
        y += 1
    if x == r + 1:
        break
    if y // x == 0:
        continue
    d = gcd(x, y)
    if d == 1 or x // d == 1 or y // d == 1:
        continue
    count += 1
print(count * 2)