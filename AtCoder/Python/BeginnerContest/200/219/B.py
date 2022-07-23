import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
for i in input().strip():
    if i == '1':
        print(s1, end='')
    elif i == '2':
        print(s2, end='')
    else:
        print(s3, end='')
