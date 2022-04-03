'''
Title : 내장함수 11
'''

dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
for k in sorted(dict.keys()):
    print('{}: {}'.format(k, dict[k]))