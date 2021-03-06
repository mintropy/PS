"""
Title : 약수 지우기 게임 1
Link : https://www.acmicpc.net/problem/12107
"""

print('A' if input().strip() != '1' else 'B')
# print('A' if int(input())>1 else 'B')


'''
n == 1 : B
n == 2 : A (1 >> 2)
n == 3 : A (3,1 or 2,1 >> 2 or 3)
n == 4 : A (4,2,1 >> 3)
n == 5 : A (2,1 >> 모든 경우)

n >= 2 일때 B가 이길 수 없나 ? : 없음
게임 case 2가지 : 1을 먼저 지우거나 아닐 때(아니라면, 1은 모든 수의 약수이므로 지워짐)
B가 이긴다고 하자
1. A가 1을 먼저 지웠다면, 반대로 다른 수를 지우면 이길 수 있음
2. A가 1이 아닌 다른 수를 먼저 지웠다면, 반대로 1을 지워서 이길 수 있음
'''