import sys

input = sys.stdin.readline

alphabet = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def solution(s, alphabet):
    l = len(s)
    for i in range(l, 0, -1):
        if s[0] == alphabet[i]:
            s = s[1:]
        elif s[-1] == alphabet[i]:
            s = s[:-1]
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    if solution(str(input()), alphabet):
        print('YES')
    else:
        print('NO')