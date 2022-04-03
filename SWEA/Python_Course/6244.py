'''
Title : 흐름과 제어 - 반복 7
'''

grade = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0
for x in grade:
    if x >= 80:
        total += x
print(total)