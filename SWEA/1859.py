'''
Title : 백만 장자 프로젝트
'''

def solution(i: int):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = 0
    m = seq.pop(-1)
    while seq:
        if m > seq[-1]:
            ans += m - seq[-1]
            seq.pop(-1)
        else:
            m = seq.pop(-1)
    print('#', i, ' ', ans, sep = '')

t = int(input())
for i in range(t):
    solution(i + 1)