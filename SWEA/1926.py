"""
Title : 간단한 369게임
"""

n = int(input())

for i in range(1, n + 1):
    turn = list(str(i))
    count = 0
    for c in turn:
        if c in ['3', '6', '9']:
            count += 1
    
    if count == 0:
        print(i, end = ' ')
    else:
        print('-' * count, end = ' ')