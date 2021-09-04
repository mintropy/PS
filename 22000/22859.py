"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = input().strip().split('<div')
ans = []

for context in html[1:]:
    tmp = context.split('<p>')
    # 제목은 따로 추가
    title = tmp[0].split('"')
    ans.append('title : ' + title[1])
    # 각 줄 추가
    # if len(tmp) > 1:
    for paragraph in tmp[1:]:
        para = ''
        st = 0
        for i in range(len(paragraph)):
            if paragraph[i] == '<':
                txt = paragraph[st:i].strip()
                if txt != ' ' * len(txt):
                    para += ' ' + paragraph[st:i].strip()
            elif paragraph[i] == '>':
                st = i + 1
        ans.append(para.strip())

print(*ans, sep='\n')


'''
# index error
html = list(input().strip().split('<'))

ans = []
for i in range(2, len(html) - 1):
    tmp = html[i].split('>')
    # div라면 title로 추가
    if len(tmp[0]) > 3 and tmp[0][:3] == 'div':
        title = tmp[0].split('"')
        ans.append('title : ' + title[1])
    elif tmp[1] == ' ' * len(tmp[1]):
        continue
    elif tmp[0] == 'p':
        ans.append(tmp[1].strip())
    else:
        ans[-1] += ' ' + tmp[1].strip()

print(*ans, sep='\n')
'''

'''
<main><div title="title"></div></main>

'''