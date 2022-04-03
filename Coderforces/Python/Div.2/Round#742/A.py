import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    s = s.replace('U', 'd')
    s = s.replace('D', 'U')
    s = s.replace('d', 'D')
    
    print(s)
