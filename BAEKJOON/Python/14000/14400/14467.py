from sys import stdin

'''
n = int(stdin.readline())
'''
n = 8

cows = [None for _ in range(11)]
count = 0

for _ in range(n):
    #cow, pos = map(int, stdin.readline().split())
    cow, pos = map(int, input().split())

    if cows[cow] == None:
        cows[cow] = pos
    elif cows[cow] == pos:
        continue
    else:
        count += 1
        cows[cow] = pos

print(count)