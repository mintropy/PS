import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    
    zeros = seq.count(0)
    ones = seq.count(1)
    print(2 ** zeros * ones)
