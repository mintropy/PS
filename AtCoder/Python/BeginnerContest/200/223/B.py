import sys
input = sys.stdin.readline


s = input().strip()

possible = []
for i in range(len(s)):
    possible.append(s)
    s = s[1:] + s[0]

possible.sort()

print(possible[0], possible[-1], sep='\n')
