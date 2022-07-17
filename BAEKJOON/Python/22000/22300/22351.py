"""
Title : 수학은 체육과목 입니다 3
Link : https://www.acmicpc.net/problem/22351
"""

# https://www.acmicpc.net/source/31679593
# 단순하지만 강력한 풀이법

import sys
input = sys.stdin.readline

def check(ans: list) -> None:
    st = 0
    # 한자리수에서 시작하는지 확인
    # 처음 4개를 확인해야 함
    if ans[0] + 1 == ans[1] and ans[1] + 1 == ans[2] and ans[2] + 1 == ans[3]:
        length = 1
        st = ans[0]
    elif ans[:4] == [7, 8, 9, 1]:
        length = 1
        st = ans[0]
    elif ans[:4] == [8, 9, 1, 0]:
        length = 1
        st = ans[0]
    elif ans[:4] == [9, 1, 0, 1]:
        length = 1
        st = ans[0]
    # 두자리수에서 시작하는 경우
    elif ans[0] * 10 + ans[1] + 1 == ans[2] * 10 + ans[3]:
        length = 2
        st = ans[0] * 10 + ans[1]
    elif ans[:4] == [9, 9, 1, 0]:
        length = 2
        st = 99
    # 아닌경우 세자리수 부터 시작
    else:
        length = 3
        st = ans[0] * 100 + ans[1] * 10 + ans[2]
    # 숫자를 하나씩 올려가며 마지막 수까지 도달
    now = st
    idx = length
    while True:
        if idx >= len(ans):
            break
        # 다음 숫자 지정
        now += 1
        if now == 10 ** length:
            length += 1
        idx += length
    print(st, now)
    return


ans = list(int(i) for i in str(input().strip()))

# 입력 길이가 1, 2일때는 따로 처리
if len(ans) == 1:
    print(ans[0], ans[0])
elif len(ans) == 2:
    # 한 자리수로 가능한지, 아닌지 판별
    i, j = ans[0], ans[1]
    if j == i + 1:
        print(i, j)
    else:
        print(i * 10 + j, i * 10 + j)
# 길이가 3인 경우
elif len(ans) == 3:
    if ans[0] + 1 == ans[1] and ans[1] + 1 == ans[2]:
        print(ans[0], ans[2])
    elif ans[0] == 9 and ans[1] * 10 + ans[2] == 10:
        print(9, 10)
    else:
        print(ans[0] * 100 + ans[1] * 10 + ans[2], ans[0] * 100 + ans[1] * 10 + ans[2])
else:
    check(ans)