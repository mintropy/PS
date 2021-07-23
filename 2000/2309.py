'''
Title : 일곱 난쟁이
Link : https://www.acmicpc.net/problem/2309
'''

def find(heights):
    total = sum(heights)
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if total - heights[i] - heights[j] == 100:
                return i, j


# heights = [int(input()) for _ in range(9)]
heights = []
for _ in range(9):
    heights.append(int(input()))
heights.sort()

fake1, fake2 = find(heights)
for i in range(9):
    if i == fake1 or i == fake2:
        continue
    print(heights[i]) 