'''
Title : 내장함수 4
'''

s = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
count = 0
for i in range(len(s)):
    if s[i] == 'A':
        count += 4
    elif s[i] == 'B':
        count += 3
    elif s[i] == 'C':
        count += 2
    else:
        count += 1
print(count)