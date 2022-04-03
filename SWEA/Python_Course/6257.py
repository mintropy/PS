'''
Title : 셋, 딕셔너리 5
'''

fruit = ['   apple    ','banana','  melon']
fruit_dic = {}
for x in fruit:
    x = x.strip()
    fruit_dic[x] = len(x)

print(fruit_dic)