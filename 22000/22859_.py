"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

# div, p태그로 split
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
