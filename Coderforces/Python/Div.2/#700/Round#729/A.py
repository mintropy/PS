import sys

input = sys.stdin.readline

# test case 
t = int(input())

for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    count_odd = 0
    for x in seq:
        if x % 2 == 1:
            count_odd += 1
    if count_odd == n:
        print("Yes")
    else:
        print("No")