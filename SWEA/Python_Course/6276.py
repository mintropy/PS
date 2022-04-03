'''
Title : 자료구조 - 리스트, 튜플 3
'''

l = [[] for _ in range(8)]

for i in range(2, 10):
    for j in range(1, 10):
        if i * j % 3 == 0 or i * j % 7 == 0:
            continue
        l[i - 2].append(i * j)
print(l)