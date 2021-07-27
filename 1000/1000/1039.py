"""
Title : 교환
Link : https://www.acmicpc.net/problem/1039
"""

import sys, collections, itertools
input = sys.stdin.readline

n, k = map(int, input().split())


# 안되는 경우부터 설정
# 한자리 수, 두자리 수이면서, 10의 배수
if n == 1:
    print(-1)
elif len(str(n)) == 2 and n % 10 == 0:
    print(-1)
else:
    max_result = -1
    nums = list(str(n))
    comb = list(itertools.combinations(range(len(nums)), 2))
    
    
    print(max_result)
