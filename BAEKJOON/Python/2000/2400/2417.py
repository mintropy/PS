"""
Title : 정수 제곱근
Link : https://www.acmicpc.net/problem/2417
"""


n = int(input())

st, end = 1, n // 2
mid = (st + end) // 2
while st <= end:
    mid = (st + end) // 2
    if mid ** 2 >= n:
        end = mid - 1
    else:
        st = mid + 1

if mid ** 2 >= n:
    print(mid)
else:
    print(mid + 1)