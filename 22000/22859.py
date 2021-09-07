"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = input().strip()
ans = []

div = False
tag = False
tmp = ' '
for i in range(len(html) - 7):
    s = html[i]
    if s == '<':
        tag = True
        # div 태그인지 확인
        if html[i + 1:i + 4] == 'div':
            div = True
        # 닫는 p태그인지 확인
        elif html[i + 1:i + 3] == '/p':
            ans.append(tmp.strip())
            tmp = ' '
    elif s == '>':
        tag = False
        # 태그가 끝날 때 div였으면 title로 추가
        if div:
            title = tmp.split('"')
            ans.append('title : ' + title[1])
            tmp = ' '
            div = False
    # div이면 내용 추가
    elif div:
        tmp += s
    # div가 아니고 다른 tag속이 아닐 때
    elif not div and not tag:
        # 빈칸이 연속되거나, 가장 앞, 뒤가 아니게
        if s == ' ' or tmp[-1] == ' ':
            continue
        tmp += s

print(*ans, sep='\n')


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
<main><p>para1</p><div title="title"><p>para2</p></div><p>para3</p></main>

'''