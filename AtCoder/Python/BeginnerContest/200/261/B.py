N = int(input())
table = [input().strip() for _ in range(N)]

counter_status = {"W": "L", "L": "W", "D": "D"}

for i in range(N):
    for j in range(i + 1, N):
        status = table[i][j]
        if table[j][i] != counter_status[status]:
            print("incorrect")
            break
    else:
        continue
    break
else:
    print("correct")
