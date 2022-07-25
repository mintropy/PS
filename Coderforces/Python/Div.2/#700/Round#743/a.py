import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    seq = list(int(i) for i in input().strip())
    count = 0
    for i in range(n - 1):
        if seq[i]:
            count += seq[i] + 1
    count += seq[n - 1]
    print(count)
