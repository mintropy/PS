import sys

input = sys.stdin.readline

while True:
    s = str(input().strip())
    if s == '0':
        break
    else:
        tf = True
        for i in range(len(s) // 2 + 1):
            if s[i] != s[-1 -i]:
                tf = False
                break
        if tf:
            print('yes')
        else:
            print('no')
