import sys
input = sys.stdin.readline


X = int(input())

if X <= 99:
    print(X)
elif len(str(X)) >= 11:
    d1 = int(str(X)[0])
    ans = int(str(d1) * len(str(X)))
    if ans >= X:
        print(ans)
    else:
        print(int(str(d1 + 1) * len(str(X))))
else:
    print()
