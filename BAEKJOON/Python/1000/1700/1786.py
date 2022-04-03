"""
Title : 찾기
Link : https://www.acmicpc.net/problem/1786
"""


def KMP(string: str, target: str):
    j = 0
    table = target_pattern(target)
    same = []
    for i in range(len(string)):
        while j > 0 and string[i] != target[j]:
            j = table[j - 1]
        # 같은 부분을 찾았을 때
        if string[i] == target[j]:
            if j == len(target) - 1:
                same.append(i - len(target) + 2)
                j = table[j]
            else:
                j += 1
    return same


def target_pattern(target):
    table = [0] * len(target)
    i = 0
    for j in range(1, len(target)):
        # if target[i] == target[j]:
        #     i += 1
        #     table[j] = i
        # else:
        #     i = 0
        while i > 0 and target[i] != target[j]:
            i = table[i - 1]
        if target[i] == target[j]:
            i += 1
            table[j] = i
    return table


string = input().rstrip()
target = input().rstrip()

same = KMP(string, target)

print(len(same))
print(*same)


'''
Counter Example
abacababacabab
abacabab
ans : 2 / 1 7
output : 2 / 1
'''