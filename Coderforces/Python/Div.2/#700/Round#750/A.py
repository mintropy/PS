import sys
input = sys.stdin.readline


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    
    if a == b and b == c:
        print(0)
        continue
    total_song = a + b * 2 + c * 3
    
    concert = total_song // 2
    
    
