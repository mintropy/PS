'''
Title : [Professional] 합
'''

test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    seq = list(map(int, input().split()))
    
    dp = []
    partial_sum = 0
    for i in range(n):
        if seq[i] >= 0:
            partial_sum += seq[i]
        elif partial_sum + seq[i] > 0:
            partial_sum += seq[i]
        else:
            partial_sum = 0
        dp.append(partial_sum)

    if max(seq) < 0:
        maximum = max(seq)
    else:
        maximum = max(dp)
    print(f'#{tc} {maximum}')