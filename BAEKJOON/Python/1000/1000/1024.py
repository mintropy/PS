"""
Title : 수열의 합
Link : https://www.acmicpc.net/problem/1024
"""

n, l = map(int, input().split())

while True:
    # l 조건 : 100 이하
    if l > 100:
        print(-1)
        break
    seq_st = n // l
    seq_st -= l // 2
    
    if seq_st < -1:
        print(-1)
        break
    
    seq_sum = sum(range(seq_st, seq_st + l))
    
    while seq_sum < n:
        if seq_sum + l <= n:
            seq_sum += l
            seq_st += 1
        else:
            break
    
    if seq_sum == n:
        print(*range(seq_st, seq_st + l))
        break
    else:
        l += 1


'''
Counter Example
5151 100
ans : -1

19 2
ans : 9 10

10 4
ans : 1 2 3 4

1 2
ans : 0 1

11 3
ans : -1
'''