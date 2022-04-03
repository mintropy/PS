'''
Title : 흐름과 제어 - 반복 6
'''

blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood_count = {'A': 0, 'B': 0, 'AB': 0, 'O' :0}
for blood_type in blood:
    blood_count[blood_type] += 1

print('{', end = '')
print("\'A\': ", blood_count['A'], ', ', sep = '',end = '')
print("\'O\': ", blood_count['O'], ', ', sep = '', end = '')
print("\'B\': ", blood_count['B'], ', ', sep = '', end = '')
print("\'AB\': ", blood_count['AB'], sep = '', end = '')
print('}')