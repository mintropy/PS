"""
Title : 로마 숫자 만들기
Link : https://www.acmicpc.net/problem/16922
"""

def find_num(left: int, num_used: list):
    global n
    if left == 0:
        count = 0
        for i in range(1, 50 * n + 1):
            if num_used[i]:
                count += 1
        return count
    new_num_used = [False] * (50 * n + 1)
    if left == n:
        new_num_used[1] = new_num_used[5] = new_num_used[10] = new_num_used[50] = True
    else:
        for i in range(50 * n, 0, -1):
            if num_used[i]:
                new_num_used[i + 1] = new_num_used[i + 5] = new_num_used[i + 10] = new_num_used[i + 50] = True
    return find_num(left - 1, new_num_used)


n = int(input())
num_used = [False] * (50 * n + 1)

print(find_num(n, num_used))
