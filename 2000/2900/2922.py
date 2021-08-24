"""
Title : 즐거운 단어
Link : https://www.acmicpc.net/problem/2922
"""

def make_word(token: list, idx: int, count: int, l_find: bool):
    global total_count
    if idx == len(token):
        if count > total_count:
            total_count = count
        return
    # 해당 idx마다 본인 포함 왼쪽, 오른쪽으로 3칸 범위까지 확인
    # 만약 0, 1, n - 2, n - 1인 경우라면, 가능한 부분까지 확인
    # 해당 위치가 공백일때만 탐색
    if token[idx]:
        make_word(token, idx + 1, count, l_find)
    else:
        # 경우의 수
        # 1. 왼쪽 2개, 오른쪽 2개, 왼쪽/오른쪽으로 같은게 있는 경우
        #   같은 분류로 넣으면 3개 연속이 됨
        # 2. 해당 범위에 같은 경우가 없음
        #   어떤 분류가 들어가던지 상관 없음
        # 해당 범위에 자음 or 모음이 연속인지 확인
        check_left = set('V', 'C')
        check_mid = set('V', 'C')
        check_right = set('V', 'C')
        # 왼쪽으로 탐색
        if idx >= 2:
            if token[idx - 1] == 'V' and token[idx - 2] == 'V':
                check_left.remove('V')
            elif token[idx - 1] in 'CL' and token[idx - 2] in 'CL':
                check_left.remove('C')
        # 왼쪽 한칸/ 오른쪽 한칸
        # 오른쪽이 비어있으면 둘 다 추가
        if idx >= 1 and idx < len(token) - 1:
            if not token[idx + 1]:
                check_mid = set('V', 'C')
            elif token[idx + 1] == 'V':
                check_mid.add('V')
            else:
                check_mid.add('C')
            if token[idx - 1] == 'V':
                check_left.add('V')
            else:
                check_left.add('C')
        # 오른쪽 두 칸 확인
        # 둘 중 하나라도 비어있으면 둘 다 추가
        # 아니면 둘 다 비교
        if idx < len(token) - 2:
            if not token[idx + 1] or not token[idx + 2]:
                check_right = set('V', 'C')
            else:
                if token[idx + 1] == 'V':
                    check_left.add('V')
                else:
                    check_left.add('C')
                if token[idx + 2] == 'V':
                    check_left.add('V')
                else:
                    check_left.add('C')
        # 가능한 경우 수 탐색
        



word = input().strip()
# 단어로 비교하는 대신 알파벳 별로 분류하여 처리
# 공백, L, 자음, 모음으로 분류
token = []
for alp in word:
    if alp in 'AEIOU':
        token.append('V')
    elif alp == '_':
        token.append('')
    elif alp == 'L':
        token.append('L')
    else:
        token.append('C')

total_count = 0

