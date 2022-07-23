L1, R1, L2, R2 = map(int, input().split())
if L1 > L2:
    L1, R1, L2, R2 = L2, R2, L1, R1

if R1 <= L2:
    print(0)
elif L2 <= R1 <= R2:
    print(R1 - L2)
else:
    print(R2 - L2)
