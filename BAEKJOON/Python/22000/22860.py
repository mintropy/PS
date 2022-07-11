"""
Title : 폴더 정리 (small)
Link : https://www.acmicpc.net/problem/22860
"""

from dataclasses import dataclass, field
from sys import stdin

input = stdin.readline


@dataclass
class Directory:
    parent: str
    files_count: int = 0
    files: set = field(default_factory=set)

    def get_different_files_count(self) -> int:
        return len(list(self.files))


def update_files(folder_name: str, file_name: str) -> None:
    global directory
    while folder_name != "main":
        parent = directory[folder_name].parent
        directory[parent].files.add(file_name)
        directory[parent].files_count += 1
        folder_name = parent


if __name__ == "__main__":
    N, M = map(int, input().split())
    directory: dict[str, Directory] = {"main": Directory(parent="")}
    folder_to_directory: dict[str, str] = {"main": "main"}
    for _ in range(N + M):
        P, F, C = input().strip().split()
        P = folder_to_directory[P]
        if C == "0":
            directory[P].files.add(F)
            directory[P].files_count += 1
            update_files(P, F)
        else:
            parent_directory = P
            child_directory = f"{parent_directory}/{F}"
            directory[child_directory] = Directory(parent=parent_directory)
            folder_to_directory[F] = child_directory
    for _ in range(int(input())):
        d = input().strip()
        print(directory[d].get_different_files_count(), directory[d].files_count)
