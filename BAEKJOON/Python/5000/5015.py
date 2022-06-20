"""
title : ls
Link : https://www.acmicpc.net/problem/5015
"""

from sys import stdin

input = stdin.readline


def search(pattern_idx: int, file_name_idx: int) -> bool:
    global pattern_length, file_name_length, pattern, file_name
    if file_name_idx == file_name_length:
        if pattern_idx == pattern_length:
            return True
        elif pattern_idx + 1 == pattern_length and pattern[pattern_idx] == "*":
            return True
        else:
            return False
    elif pattern_idx == pattern_length:
        return False
    if pattern[pattern_idx] == "*":
        if search(pattern_idx + 1, file_name_idx):
            return True
        if search(pattern_idx, file_name_idx + 1):
            return True
        if search(pattern_idx + 1, file_name_idx + 1):
            return True
        return False
    else:
        if pattern[pattern_idx] == file_name[file_name_idx]:
            if search(pattern_idx + 1, file_name_idx + 1):
                return True
            return False
        else:
            return False


if __name__ == "__main__":
    pattern = input().strip()
    pattern_length = len(pattern)
    for _ in range(int(input())):
        file_name = input().strip()
        file_name_length = len(file_name)
        if search(0, 0):
            print(file_name)
