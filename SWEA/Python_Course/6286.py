'''
Title : 자료구조 - 리스트, 튜플 11
'''

l = [1, 1]
for _ in range(3, 11):
    l.append(l[-1] + l[-2])
print(l)