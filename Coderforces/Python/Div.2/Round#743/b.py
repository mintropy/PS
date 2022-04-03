import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    seq_a = list(map(int, input().split()))
    seq_b = list(map(int, input().split()))
    
    if seq_a < seq_b:
        print(0)
    else:
        for i in range(n):
            if seq_b[i] > seq_a[0]:
                move_a_only = i
                break
        for i in range(n):
            if seq_a[i] < seq_b[0]:
                move_b_only = i
                break
        print(min(move_a_only, move_b_only))
