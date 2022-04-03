'''
Title : 햄버거
Link : https://www.acmicpc.net/problem/19941
'''

from itertools import permutations
import sys, collections

input = sys.stdin.readline

n, k = map(int, input().split())
s = str(input().strip())

people_check = 0
people = collections.deque([])
hamburgers = collections.deque([])

for i in range(n):
    if s[i] == 'H':
        hamburgers.append(i)
        while people:
            person = people.popleft()
            if i - person > k:
                continue
            elif i - person <= k:
                hamburgers.popleft()
                people_check += 1
                break            
    elif s[i] == 'P':
        people.append(i)
        while hamburgers:
            hamburger = hamburgers.popleft()
            if i - hamburger > k:
                continue
            elif i - hamburger <= k:
                people.popleft()
                people_check += 1
                break



print(people_check)
