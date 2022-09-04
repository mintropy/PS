"""
Title : Hashing
Link : https://www.acmicpc.net/problem/15829
"""

# import sys
# from string import ascii_lowercase

# alp_num = {alp: num + 1 for num, alp in enumerate(list(ascii_lowercase))}


l = int(input())
s = input()

r = 1
ans = 0
for i in range(l):
    ans += ((ord(s[i]) - 96) * r)
    r = (r * 31) % 1234567891

print(ans % 1234567891)