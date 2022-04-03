'''
Title : 자료구조 - 리스트, 튜플 19
'''

word = list(map(str , input().split(', ')))
word.sort()

for i in range(len(word) - 1):
    print(word[i], ', ', sep = '', end = '')
print(word[-1])