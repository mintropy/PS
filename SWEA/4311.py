"""
Titel : 오래된 스마트폰
"""

import collections


def DFS(eq_now: int):
    global m, possible_operator, all_possible_num, count
    num_now = eval(eq_now)
    # 불가능
    if num_now >= 1000 or num_now < 0:
        return
    if len(eq_now) > m:
        return
    # 탐색 필요 ㄴㄴ
    if count[num_now] < len(eq_now):
        return
    count[num_now] = len(eq_now)
    # 탐색
    # 연산자 하나 뽑고, 숫자 하나 뽑아서 탐색
    for op in possible_operator:
        for num in all_possible_num:
            # 순서대로 +, -, *, /
            if op == 1:
                DFS(eq_now + '+' + num)
            elif op == 2:
                DFS(eq_now + '-' + num)
            elif op == 3:
                DFS(eq_now + '*' + num)
            else:
                if num == '0':
                    continue
                DFS(eq_now + '//' + num)


for tc in range(1, int(input()) + 1):
    n, o, m = map(int, input().split())
    possible_num = list(input().strip().split())
    possible_operator = list(map(int, input().split()))
    
    target_num = int(input())
    count = [1000] * 1000
    
    # 가능한 한자리수 번호로 만들 수 있는 모든 1, 2, 3자리수
    all_possible_num = [possible_num[::], [], []]
    for x in possible_num:
        if x == '0':
            continue
        for num in all_possible_num[0]:
            all_possible_num[1].append(x + num)
    for x in possible_num:
        if x == '0':
            continue
        for num in all_possible_num[1]:
            all_possible_num[2].append(x + num)
    all_possible_num = sum(all_possible_num, start=[])
    for num in all_possible_num:
        count[int(num)] = len(num)
    
    if count[target_num] != 1000:
        print(f'#{tc} {len(str(target_num))}')
    else:
        for num in all_possible_num:
            DFS(num)
        if count[m] == 1000:
            print(f'#{tc} {-1}')
        else:
            print(f'#{tc} {count[target_num] + 1}')
