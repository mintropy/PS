"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = list(input().strip().split('<'))

ans = []
for i in range(2, len(html)):
    # div, main닫는 태그면 넘어가기
    if html[i][0] == '/':
        if html[i][1] == 'i' or html[i][1] == 'b':
            tmp = html[i][3:].strip()
            if tmp:
                ans[-1] += ' ' + tmp
        else:
            continue
    # div 태그면 title로 바로 추가
    elif html[i][0] == 'd':
        ans.append('title : ' + html[i][11:-2])
    # p태그이면 새롭게 추가, 아니면 같은 줄이므로, 공백 후 이전 내용에 추가
    elif html[i][0] == 'p':
        ans.append(html[i][2:].strip())
    elif html[i][0:2] == 'br':
        tmp = html[i][4:].strip()
        if tmp:
            ans[-1] += ' ' + tmp
    else:
        tmp = html[i][2:].strip()
        if tmp:
            ans[-1] += ' ' + tmp

for line in ans:
    if line:
        print(line)
