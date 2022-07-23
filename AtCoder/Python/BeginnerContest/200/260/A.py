S = input().strip()

for x in S:
    if S.count(x) == 1:
        print(x)
        break
else:
    print(-1)
