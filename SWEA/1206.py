'''
Title : View
'''

for i in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))

    ans = 0
    for j in range(2, n - 2):
        next = max(buildings[j - 2], buildings[j - 1], buildings[j + 1], buildings[j + 2])
        if buildings[j] < next:
            continue
        else:
            ans += buildings[j] - next
    
    print('#', i, ' ', ans, sep = '')