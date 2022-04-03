import sys

input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n - 1):
    t1, l1, r1 = array[i]
    for j in range(i + 1, n):
        t2, l2, r2 = array[j]
        if r2 < l1 or l2 > r1:
            continue
        elif l1 <= l2 and r1 >= r2:
            ans += 1
        elif r2 <= r1:
            if t1 == 1 or t1 == 2:
                if t2 == 1 or t2 == 3:
                    ans += 1
                elif t2 == 2 or t2 == 4:
                    if r2 > l1:
                        ans += 1
            elif t1 == 3 or t1 == 4:
                if r2 > l1:
                    ans += 1
        elif l2 >= l1:
            if t1 == 1 or t1 == 3:
                if t2 == 1 or t2 == 2:
                    ans += 1
                elif t2 == 3 or t2 == 4:
                    if r2 < l1:
                        ans += 1
            elif t1 == 2 or t1 == 4:
                if r2 < l1:
                    ans += 1

print(ans)