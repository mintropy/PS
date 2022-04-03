'''
Title : 자료구조 - 리스트, 튜플 8
'''

tmp = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
l = []
for x in tmp:
    if x % 2 == 0:
        l.append(x)
print(l)