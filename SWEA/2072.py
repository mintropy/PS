'''
Title : 홀수만 더하기
'''

test_case = int(input())

for tc in range(1, test_case + 1):
    seq = list(map(int, input().split()))
    seq_sum = 0
    for x in seq:
        if x % 2 != 0:
            seq_sum += x
    print(f'#{tc} {seq_sum}')