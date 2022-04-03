'''
Title : 슈퍼마리오
Link : https://www.acmicpc.net/problem/2851
'''

mushrooms = [int(input()) for _ in range(10)]

answer = 0
score = 0
for i in range(10):
    score += mushrooms[i]
    if score > 100 + abs(100 - answer):
        break
    if abs(100 - score) < (100 - answer):
        answer = score
    elif abs(100 - score) == (100 - answer) and score > answer:
        answer = score

print(answer)