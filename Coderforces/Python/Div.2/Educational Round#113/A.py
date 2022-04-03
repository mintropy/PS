import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    if n == 1:
        print(-1, -1)
    else:
        flag = False
        for k in range(n // 2):
            if flag:
                break
            for i in range(n - (k + 1) * 2 + 1):
                if s[i:i + k].count('a') == k:
                    print(i + 1, i + (k + 1) * 2)
                    flag = True
                    break
        else:
            print(-1, -1)
