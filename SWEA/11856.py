'''
Title : 반반
'''

test_case = int(input())
for tc in range(1, test_case + 1):
    s = str(input())
    d = {}
    for i in range(4):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    
    if len(d.keys()) != 2:
        print(f'#{tc} No')
    else:
        if d[list(d.keys())[0]] == 2 and d[list(d.keys())[1]] == 2:
            print(f'#{tc} Yes')
        else:
            print(f'#{tc} No')
