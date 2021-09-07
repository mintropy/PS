"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = input().strip()




'''
html = input().strip().split('<div')

lines = []
for i in range(1, len(html)):
    lines.append(html[i].split('<p>'))

ans = []
for div in lines:
    if 'title="'in div[0]:
        title = div[0].split('"')
        ans.append('title : ' + title[1])
        st = 1
    else:
        st = 0
    
    for i in range(st, len(div)):
        paragraph = div[i]
        tmp = ''
        tag = False
        for s in paragraph:
            if s == '<':
                tag = True
            elif s == '>':
                tag = False
            elif tag:
                continue
            else:
                if s == ' ':
                    if len(tmp) == 0 or tmp[-1] == ' ':
                        continue
                tmp += s
        if tmp:
            ans.append(tmp)

print(*ans, sep='\n')
'''


'''
# index error?
html = input().strip().split('<div')
ans = []

for context in html[1:]:
    if not context:
        continue
    tmp = context.split('<p>')
    # 제목은 따로 추가
    title = tmp[0].split('"')
    ans.append('title : ' + title[1])
    if len(context) == 1:
        continue
    # 각 줄 추가
    for paragraph in tmp[1:]:
        para = ''
        tag = False
        for i in range(len(paragraph)):
            if paragraph[i] == '>':
                tag = False
            elif paragraph[i] == '<' or tag:
                tag = True
                continue
            else:
                c = paragraph[i]
                if c == ' ':
                    if not para or para[-1] == ' ':
                        continue
                para += c
        para.strip()
        if para:
            ans.append(para)

print(*ans, sep='\n')
'''

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
<main><div title="title"></div><p>para</p></main>

'''