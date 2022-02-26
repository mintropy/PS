"""
Title : 가르침
Link : https://www.acmicpc.net/problem/1062
"""

import sys
input = sys.stdin.readline


def dfs(count, words, check, alphabets, limit):
    max_count = count
    for i in range(len(words)):
        if check[i]:
            continue
        alp_count = 0
        for s in words[i]:
            if not alphabets[s]:
                alp_count += 1
        if alp_count <= limit:
            for s in words[i]:
                alphabets[s] = True
            check[i] = True
            tmp = dfs(count + 1, words, check, alphabets, limit - alp_count)
            if max_count < tmp:
                max_count = tmp
            for s in words[i]:
                alphabets[s] = False
            check[i] = False
    return max_count


def solution():
    N, K = map(int, input().split())
    alphabets = [False] * 26
    alphabets[ord('a') - 97] = alphabets[ord('c') - 97] = alphabets[ord('n') - 97]\
        = alphabets[ord('i') - 97] = alphabets[ord('t') - 97] = True

    words = []
    for _ in range(N):
        word = input().strip()[4:-4]
        words.append(set(ord(s) - 97 for s in word))

    print(dfs(0, words, [False] * N, alphabets, K - 5))


solution()


'''
Counter Example


'''
