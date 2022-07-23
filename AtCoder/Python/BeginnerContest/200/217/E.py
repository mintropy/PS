import sys
input = sys.stdin.readline

q = int(input())
seq = []

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        seq.append(query[1])
    elif query[0] == 2:
        print(seq[0])
        seq = seq[1:]
    else:
        seq.sort()
