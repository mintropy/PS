'''
Title : 문자열 3
'''

url = list(map(str, input().split('/')))
print('protocol:', url[0][:-1])
print('host:', url[2])
print('others:', url[3])