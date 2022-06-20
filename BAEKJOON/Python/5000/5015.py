"""
title : ls
Link : https://www.acmicpc.net/problem/5015
"""

from sys import stdin

input = stdin.readline


def search(pattern_idx: int, file_name_idx: int) -> bool:
    global pattern_length, file_name_length, pattern, file_name, check
    if pattern_idx == pattern_length and file_name_idx == file_name_length:
        return True
    if pattern_idx == pattern_length:
        return False
    if file_name_idx == file_name_length:
        if pattern[pattern_idx] != "*":
            return False
        else:
            if search(pattern_idx + 1, file_name_idx):
                return True
            return False
    if check[pattern_idx][file_name_idx]:
        return check[pattern_idx][file_name_idx]
    if pattern[pattern_idx] == "*":
        result = False
        if search(pattern_idx + 1, file_name_idx):
            result = True
        if search(pattern_idx, file_name_idx + 1):
            result = True
        if search(pattern_idx + 1, file_name_idx + 1):
            result = True
        check[pattern_idx][file_name_idx] = result
        return result
    else:
        if pattern[pattern_idx] == file_name[file_name_idx]:
            if search(pattern_idx + 1, file_name_idx + 1):
                check[pattern_idx][file_name_idx] = True
                return True
        return False


if __name__ == "__main__":
    pattern = input().strip()
    pattern_length = len(pattern)
    answer = ""
    for _ in range(int(input())):
        file_name = input().strip()
        file_name_length = len(file_name)
        check = [[False] * file_name_length for _ in range(pattern_length)]
        if search(0, 0):
            answer += f"{file_name}\n"
    print(answer)
