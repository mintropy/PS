'''
Title : [S/W 문제해결 기본] 1일자 - 최빈수 구하기
'''

test_case = int(input())
for _ in range(1, test_case + 1):
    tc = int(input())
    grade = list(map(int, input().split()))

    mcv = -1
    max_count = -1
    for i in range(101):
        num_count = grade.count(i)
        if num_count >= max_count:
            max_count = num_count
            mcv = i

    print(f'#{tc} {mcv}')