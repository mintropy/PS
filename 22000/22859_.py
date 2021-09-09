"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

'''
1. div 태그의 title
2. p태그 처리
    1. p태그 내부 태그 제거
    2. p태그 문장 시작 끝 공백 제거
    3. 공백 2개 이상 연속 >> 1개
    4. p태그 지우기
'''

def make_paragraph(paragraph: list) -> str:
    para = ''
    for p in paragraph:
        if p == ' ':
            if not para or para[-1] == ' ':
                continue
        para += p
    return para


html = input().strip().split('<div')
lines = []
for h in html:
    lines.extend(h.split('<p>'))

ans = []
for line in lines[1:]:
    # div 속성으로 반드시 title이 존재
    if 'title="' in line:
        title = line.split('"')
        # ans.append('title : ' + title[1])
        print('title : ' + title[1])
    else:
        tmp = ' '
        # 태그 내부인지 아닌지
        is_in_tag = False
        for s in line:
            if s == '<':
                is_in_tag = True
            elif s == '>':
                is_in_tag = False
            elif not is_in_tag:
                # 연속된 공백 없도록
                if s == ' ' and tmp[-1] == ' ':
                    continue
                tmp += s
        # 앞/뒤 공백 없게
        tmp = tmp.strip()
        if tmp:
            print(tmp)
