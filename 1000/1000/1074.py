"""
Title : Z
Link : https://www.acmicpc.net/problem/1074
"""

n, r, c = map(int, input().split())
r += 1
c += 1

# 분할된 사각형에서 시작하는 숫자
st_num = 0
# 전체 크기
total_size = 2 ** (n - 1)

while total_size > 1:
    # 4분할 중 어디인지 확인
    if r <= total_size:
        row_st = 0
    else: 
        row_st = total_size
        r -= total_size
        st_num += 2 * (total_size ** 2)
    if c <= total_size:
        col_st = 0
    else: 
        col_st = total_size
        c -= total_size
        st_num += total_size ** 2
    total_size //= 2

# 마지막 세부 조정
if c == 2:
    st_num += 1
if r == 2:
    st_num += 2
print(st_num)