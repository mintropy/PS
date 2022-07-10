'''
Title : 별
Link : https://www.acmicpc.net/problem/16505
'''

def star(n, stars):
    if n == 0:
        return stars
    new = []
    for s in stars:
        if s == '*':
            new.append('**')
            new.append('*')
        else:
            # 추가 첫 줄
            new_line = ''
            for i in range(len(s)):
                if s[i] == '*':
                    new_line += '**'
                elif s[i] == ' ':
                    new_line += '  '
            new.append(new_line)
            # 추가 두번째 줄
            new_line = ''
            for i in range(len(s)):
                if s[i] == '*' and i == (len(s) - 1):
                    new_line += '*'
                elif s[i] == '*':
                    new_line += '* '
                elif s[i] == ' ':
                    new_line += '  '
            new.append(new_line)
    return star(n - 1, new)

n = int(input())
stars = ['*']
new_stars = star(n, stars)
for s in new_stars:
    print(s)