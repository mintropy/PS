import sys

input = lambda : sys.stdin.readline()


m = int(input().strip())
func = [0] + list(map(int, input().split()))

log = 20
table = [[0] * log for _ in range(m + 1)]
for i in range(1, m + 1):
    table[i][0] = func[i]

for i in range(log - 1):
    for j in range(1, m + 1):
        table[j][i + 1] = table[table[j][i]][i]


def solution():
    n, x = map(int, input().split())
    idx = 0
    while n != 0:
        if n % 2:
            x = table[x][idx]
        n //= 2
        idx += 1
    print(x)

q = int(input().strip())

for _ in range(q):
    solution()
    
