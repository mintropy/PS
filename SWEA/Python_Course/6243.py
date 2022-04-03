'''
Title : 문자열 5
'''

words = list(map(str, input().split()))
words.sort()
words = list(set(words))

for i in range(len(words) - 1):
    print(words[i], ',', sep = '', end = '')
print(words[-1])