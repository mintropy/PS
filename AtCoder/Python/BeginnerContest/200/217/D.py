import sys, bisect
input = sys.stdin.readline

l, q = map(int, input().split())

mark = [0]
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort_left(mark, x)
    else:
        idx = bisect.bisect_left(mark, x)
        if idx == len(mark):
            print(l - mark[-1])
        else:
            print(mark[idx] - mark[idx - 1])
