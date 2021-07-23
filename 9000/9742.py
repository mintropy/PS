'''
Title : 순열
Link : https://www.acmicpc.net/problem/9742
'''

def permutaion(s, n):
    seq = []
    for i in range(len(s)):
        seq.append(s[i])
    seq.sort()



while True:
    try:
        s, n = map(str, input().split())
        n = int(n)



    except:
        break

