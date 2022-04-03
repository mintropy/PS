'''
Title : 자료구조 - 리스트, 튜플 12
'''

l = []
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        continue
    l.append(i ** 2)
print(l)