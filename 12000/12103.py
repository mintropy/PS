"""
Title : 짝합 수열
Link : https://www.acmicpc.net/problem/12103
"""

import sys
sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

# 처음 k-짝합 수열인지 확인
odd, even = 0, 0
for i in range(k):
    if seq[i] % 2 == 0:
        even += 1
    else:
        odd += 1

# 처음 k개가 짝합수열일때, 아닐때로 나누어 탐색
if odd % 2 == 0:
    # 처음 k개가 짝합수열이면 바로 탐색
    changed = 0
    st = 1 if seq[0] % 2 == 1 else 0
    for i in range(k, n):
        if st:
            odd -= 1
        else:
            even -= 1
        if seq[i] % 2 == 1:
            odd += 1
        else:
            even += 1
        st = 1 if seq[i - k + 1] % 2 == 1 else 0
        
        if odd % 2 != 1:
            changed += 1
            if seq[i]:
                seq[i] -= 1
            else:
                seq[i] += 1
    print(changed)
    print(*seq)
else:
    # 처음 k개가 짝합수열이 아닐 때
    # 0번 인덱스, k-1번 인덱스를 바꾸는 두 가지로 탐색
    seq2 = seq[::]
    if seq[0]:
        seq[0] -= 1
    else:
        seq[0] += 1
    if seq2[k - 1]:
        seq2[k - 1] -= 1
    else:
        seq2[k - 1] += 1
    odd2, even2 = odd, even
    changed, changed2 = 1, 1
    st = 1 if seq[0] % 2 == 1 else 0
    st2 = 1 if seq2[0] % 2 == 1 else 0
    # 두개를 같이 탐색
    for i in range(k, n):
        if st:
            odd -= 1
        else:
            even -= 1
        if st2:
            odd2 -= 1
        else:
            even2 -= 1
        
        if seq[i] % 2 == 1:
            odd += 1
        else:
            even += 1
        if seq2[i] % 2 == 1:
            odd2 += 1
        else:
            even2 += 1
        
        st = 1 if seq[i - k + 1] % 2 == 1 else 0
        st2 = 1 if seq[i - k + 1] % 2 == 1 else 0
        
        if odd % 2 != 1:
            changed += 1
            if seq[i]:
                seq[i] -= 1
            else:
                seq[i] += 1
        if odd2 % 2 != 1:
            changed2 += 1
            if seq2[i]:
                seq2[i] -= 1
            else:
                seq2[i] += 1
    
    if changed <= changed2:
        print(changed)
        print(*seq)
    else:
        print(changed2)
        print(*seq2)
