import sys
input = sys.stdin.readline

x = list(input().strip())
order = {chr(97 + i):0 for i in range(26)}
for i in range(26):
    order[x[i]] = i

original_names = []
names = []
n = int(input())
for i in range(n):
    name = input().strip()
    original_names.append(name)
    tmp = []
    for s in name:
        tmp.append(order[s])
    name_by_order = [tmp , i]
    names.append(name_by_order)

names.sort(key=lambda x:[x[0], len(x[0])])
for i in range(n):
    print(original_names[names[i][-1]])
