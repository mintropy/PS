'''
Title : 자료구조 - 리스트, 튜플 18
'''

n, m = map(int, input().split(','))

ans = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(i * j)
    ans.append(tmp)
print(ans)