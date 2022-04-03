'''
Title : [S/W 문제해결 기본] 1일자 - 최빈수 구하기
'''

# collections.Counter 사용하여 풀이

from collections import Counter

test_case = int(input())
for _ in range(1, test_case + 1):
    tc = int(input())
    grade = list(map(int, input().split()))
    grade_dic = Counter(grade)
    max_count = sorted(grade_dic.values())[-1]
    for i in sorted(grade_dic.keys(), reverse = True):
        if grade_dic[i] == max_count:
            mcv = i
            break
    print(f'#{tc} {mcv}')