'''
Title : 책 페이지
Link : https://www.acmicpc.net/problem/1019
'''

import sys
input = sys.stdin.readline

n = int(input())
# 각 숫자별 사용된 개수
nums = [0] * 10

if n < 10:
    for i in range(10):
        if i == 0:
            print(0, end = ' ')
        elif i > n:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
else:
    # 각 자리수별로 0 ~ 9 사용 개수 저장
    num_by_len = []
    # 특정 자리수일 때 0 ~ 9 사용 개수
    # 한 자리수일 때는 위의 if 에서 처리
    # 해당 자리수 숫자 개수, 한 자리부터 시작
    for i in range(1, len(str(n))):
        # 한 자리 수일 때, 임의 생성
        if i == 1:
            count = 9
            num_len = [1] * 10
            num_len[0] = 0
            count *= 10
        # 두 자리 수 이상일 때 계산
        else:
            # 각 자리 처음부터 끝까지 사용하므로, 1 ~ 9 사용개수 같음
            # 각 자리수에 나와야 하는 숫자들의 총 개수
            total_count = count * i
            # 1이 나오는 개수 확인 == 2 ~ 9가 각각 나오는 갯수
            count_1 = 0
            for tmp in num_by_len:
                count_1 += tmp[1]
            # 각각 첫 자리가 1 ~ 9로 시작할 때 갯수
            count_1 *= 9
            # 첫 자리가 등장하는 갯수 더하기
            count_1 += 10 ** (i - 1)
            # 0이 등장하는 횟수 = 전체 개수 - 1 ~ 9 등장하는 횟수
            count_0 = total_count - count_1 * 9    
            # i자리일 때 등장하는 숫자 개수
            num_len = [count_1] * 10
            num_len[0] = count_0
        # 전체 확인할 숫자 개수 nums에 추가
        for j in range(10):
            nums[j] += num_len[j]
        # 각 자리수에서 계산한만큼 num_by_len_에 추가
        num_by_len.append(num_len)
    # 최대 자리수 이전까지 완료
    # 계산하지 못한 최대 자리수일 때 
    # n의 1의 자리수부터 0으로 만들며 진행
    num_by_digit = [int(i) for i in str(n)]
    # 지금 보고 있는 자리
    digit = 1
    for i in range(len(str(n))):
        # 해당 자리수가 내려가며, 앞의 숫자가 더해지는 만큼 else_count
        # 해당 자리수와 그 이하의 개수 확인하여 0 더하는 want_count
        else_count = num_by_digit[-digit] * (10 ** (digit - 1))
        if digit == 1:
            else_count += 1
            want_count = 0
        else:
            want_count = else_count * digit
        # 0확인 위한 tmp_count
        tmp_count = [0] * 10
        for k in range(num_by_digit[-digit], 0, -1):
            nums[k] += num_by_len[digit - 2][k]
            tmp_count[k] += num_by_len[digit -2][k]
        # 더해진 숫자를 확인, 0 개수 추가
        count_more_1 = sum(tmp_count)
        tmp_count[0] += want_count - count_more_1
        # 더 앞의 자리수 더하기
        for k in num_by_digit[-digit -1:-1:-1]:
            nums += else_count * k
        # 자리수 더하기
        digit += 1

for num in nums:
    print(num, end = ' ')

'''
# 브루트 포스 : 시간초과
for page in range(1, n + 1):
    page_in_num = list(int(p) for p in str(page))
    for p in page_in_num:
        nums[p] += 1

for num in nums:
    print(num, end = ' ')
'''

'''
n = int(sys.stdin.readline())
digits = [0]
while True:
    x = n % 10
    n //= 10
    digits.append(x)
    if n == 0:
        break

# 숫자별 사용된 개수
num = [0] * 10
base = [1] * 10

# i자리 수에서 각 수가 나오는 개수 (1 ~ 9)
num_count = [0] * 10
num_count[1] = 1
for i in range(2, 10):
    num_count[i] = 10 ** (i - 1) + num_count[i - 1] * 9

# 0부터 9까지 나오는 개수 확인
for i in range(1, len(digits)):
    n_th_digit = digits[i]
    count = 0
    if i == len(digits) - 1:
        target = 0
        for k in range(i):
            if k == i - 1:
                target += 9 * (10 ** k) * (i - 1) * (n_th_digit - 1) + 1
            else:
                target += 9 * (10 ** k) * i
    else:
        target = n_th_digit * (10 ** (i - 1)) * i
    for j in range(1, 10):
        if j > n_th_digit:
            num[j] += n_th_digit * num_count[i - 1]
        elif j == n_th_digit:
            num[j] += 1 + n_th_digit * num_count[i - 1]
            count += 1 + n_th_digit * num_count[i - 1]
        elif j < n_th_digit:
            num[j] += 10 ** (i - 1) + num_count[i - 1]
            count += 10 ** (i - 1) + num_count[i - 1]
    num[0] += target - count

for x in num:
    print(x, end = ' ')
'''