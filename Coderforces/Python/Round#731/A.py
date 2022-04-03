import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    _ = input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    if xa == xb and xa == xf:
        if yb < ya:
            ya, yb = yb, ya
        if ya < yf < yb:
            print(abs(xa - xb) + abs(ya - yb) + 2)
        else:
            print(abs(xa - xb) + abs(ya - yb)) 
    elif ya == yb:
        if xb < xa:
            xa, xb = xb, xa
        if xa < xf < xb:
            print(abs(xa - xb) + abs(ya - yb) + 2)
        else:
            print(abs(xa - xb) + abs(ya - yb)) 
    else:
        print(abs(xa - xb) + abs(ya - yb))