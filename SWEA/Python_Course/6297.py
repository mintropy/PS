'''
Title : 자료구조 - 리스트, 튜플 20
'''

l = list(map(int, input().split(',')))
l2 = []
for x in l:
    if x % 2 == 1:
        l2.append(x)

for i in range(len(l2) - 1):
    print(l2[i], ', ', sep = '', end = '')
print(l2[-1])