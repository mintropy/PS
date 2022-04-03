'''
Title : 셋, 딕셔너리 8
'''

beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer2 = {}
for key in beer.keys():
    beer2[key] = beer[key] * 1.05

print(beer)
print(beer2)