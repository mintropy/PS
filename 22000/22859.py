"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = list(input().strip().split('<'))

ans = []
for i in range(2, len(html) - 1):
    # div, main닫는 태그면 넘어가기
    if html[i][0] == '/':
        if html[i][1] == 'i' or html[i][1] == 'b':
            _, tmp = html[i].split('>')
            if tmp != ' ' * len(tmp):
                ans[-1] += ' ' + tmp.strip()
        else:
            continue
    # div 태그면 title로 바로 추가
    elif html[i][0] == 'd':
        tmp = html[i].split('"')
        ans.append('title : ' + tmp[1])
    # p태그이면 새롭게 추가, 아니면 같은 줄이므로, 공백 후 이전 내용에 추가
    elif html[i][0] == 'p':
        _, tmp = html[i].split('>')
        ans.append(tmp.strip())
    # i, br 태그일 때
    else:
        _, tmp = html[i].split('>')
        if tmp != ' ' * len(tmp):
            ans[-1] += ' ' + tmp.strip()

print(*ans, sep='\n')
